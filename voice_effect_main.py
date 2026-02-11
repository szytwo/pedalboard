import pedalboard
from pedalboard import (
    Pedalboard,
    Reverb,
    Compressor,
    Gain,
    Chorus,
    Delay,
    HighpassFilter,
    LowpassFilter,
    PeakFilter,
    Distortion,
    Mix,
    Limiter,
)
from pedalboard.io import AudioFile
import os

# -----------------------------
# 1. 播音室干声
# -----------------------------
studio_clean = Pedalboard(
    [
        HighpassFilter(80),
        PeakFilter(3000, 3, 1.0),
        Compressor(threshold_db=-22, ratio=3),
        Gain(2),
    ]
)

# -----------------------------
# 2. 舞台主持
# -----------------------------
stage_host = Pedalboard(
    [
        HighpassFilter(90),
        PeakFilter(2800, 4, 0.9),
        PeakFilter(180, 2, 0.8),
        Distortion(2),
        Compressor(threshold_db=-18, ratio=4),
        Reverb(room_size=0.35, wet_level=0.25),
        Gain(3),
    ]
)

# -----------------------------
# 3. 激情演讲
# -----------------------------
motivational = Pedalboard(
    [
        PeakFilter(160, 3, 0.8),
        PeakFilter(3000, 5, 1.0),
        Distortion(3),
        Compressor(threshold_db=-20, ratio=5),
        Reverb(room_size=0.55, wet_level=0.3),
        Delay(delay_seconds=0.12, feedback=0.2, mix=0.15),
        Gain(4),
    ]
)

# -----------------------------
# 4. 内心独白
# -----------------------------
inner_voice = Pedalboard(
    [
        Reverb(room_size=0.6, wet_level=0.4, damping=0.4),
        Chorus(rate_hz=0.6, depth=0.3, mix=0.2),
        Compressor(threshold_db=-25, ratio=3),
    ]
)

# -----------------------------
# 5. 广播电台
# -----------------------------
radio = Pedalboard(
    [
        HighpassFilter(120),
        LowpassFilter(5000),
        Distortion(4),
        Compressor(threshold_db=-16, ratio=5),
        Gain(3),
    ]
)
radio_voice = Pedalboard(
    [
        HighpassFilter(70),
        PeakFilter(120, 4, 0.9),
        PeakFilter(3200, 5, 1.0),
        Compressor(threshold_db=-18, ratio=4, attack_ms=5, release_ms=120),
        Reverb(room_size=0.3, wet_level=0.15),
    ]
)

# -----------------------------
# 6. 影视旁白
# -----------------------------
cinematic = Pedalboard(
    [
        PeakFilter(150, 2, 0.8),
        PeakFilter(2500, 3, 1.0),
        Compressor(threshold_db=-24, ratio=3),
        Reverb(room_size=0.45, wet_level=0.25),
        Gain(2),
    ]
)

# -----------------------------
# 7. 喇叭扩音
# -----------------------------
megaphone = Pedalboard(
    [
        HighpassFilter(350),
        LowpassFilter(3500),
        Distortion(6),
        Compressor(threshold_db=-18, ratio=6),
        Gain(4),
    ]
)

# -----------------------------
# 8. AI机械语音
# -----------------------------
ai_voice = Pedalboard(
    [
        HighpassFilter(150),
        PeakFilter(3500, 5, 1.2),
        Chorus(rate_hz=2.0, depth=0.15, mix=0.25),
        Compressor(threshold_db=-20, ratio=4),
    ]
)

# -----------------------------
# 9. 梦境空间
# -----------------------------
dream_voice = Pedalboard(
    [
        Reverb(room_size=0.8, wet_level=0.6),
        Chorus(rate_hz=0.8, depth=0.4, mix=0.3),
        Delay(delay_seconds=0.25, feedback=0.4, mix=0.3),
    ]
)

# -----------------------------
# 10. 游戏NPC
# -----------------------------
game_npc = Pedalboard(
    [
        PeakFilter(2000, 4, 1.1),
        Distortion(2),
        Compressor(threshold_db=-22, ratio=4),
        Chorus(rate_hz=1.5, depth=0.25, mix=0.15),
    ]
)

# 智能人声
capcut_pro_voice = Pedalboard(
    [
        # =====================
        # 🎤 ① 预处理清理
        # =====================
        # 去超低频
        HighpassFilter(70),
        # 去刺耳齿音区
        PeakFilter(6500, -2, 1.2),
        # 去浑浊
        PeakFilter(300, -2.5, 1.0),
        # =====================
        # 🎤 ② 语音塑形 EQ
        # =====================
        # 贴麦厚度
        PeakFilter(140, 3.5, 0.9),
        # 清晰存在感
        PeakFilter(3200, 4.5, 1.1),
        # 空气感
        PeakFilter(9000, 2.5, 0.8),
        # =====================
        # 🎤 ③ 动态控制
        # （模拟多段压缩）
        # =====================
        # 轻压缩控制整体
        Compressor(threshold_db=-24, ratio=2.5, attack_ms=8, release_ms=120),
        # 主压缩（语音稳定核心）
        Compressor(threshold_db=-18, ratio=4, attack_ms=4, release_ms=100),
        # =====================
        # 🎤 ④ 密度增强（剪映秘密武器）
        # =====================
        Distortion(drive_db=2.5),
        # =====================
        # 🎤 ⑤ 并行空间设计
        # =====================
        Mix(
            [
                # 干声
                Pedalboard([Gain(0)]),
                # 短房间混响
                Pedalboard(
                    [Reverb(room_size=0.32, wet_level=0.18, damping=0.6, width=0.8)]
                ),
                # 微延迟扩展声像
                Pedalboard([Delay(delay_seconds=0.08, feedback=0.15, mix=0.12)]),
            ]
        ),
        # =====================
        # 🎤 ⑥ Loudness & 最终整形
        # =====================
        Limiter(threshold_db=-1.0),
        Gain(3.5),
    ]
)

# 激情演讲
voice_speech = Pedalboard(
    [
        HighpassFilter(80),
        PeakFilter(3200, 6, 1.0),
        PeakFilter(160, 4, 0.8),
        Compressor(-22, 3.5, 4, 110),
        Compressor(-18, 5, 3, 100),
        Distortion(4),
        Mix(
            [
                Pedalboard([Gain(0)]),
                Pedalboard([Reverb(room_size=0.45, wet_level=0.28, damping=0.6, width=0.9)]),
                Pedalboard([Delay(0.12, 0.25, 0.18)]),
            ]
        ),
        Limiter(-1),
        Gain(4.5),
    ]
)

# 统一字典
VOICE_PRESETS = {
    "studio_clean": studio_clean,
    "stage_host": stage_host,
    "motivational": motivational,
    "inner_voice": inner_voice,
    "radio": radio,
    "radio_voice": radio_voice,
    "cinematic": cinematic,
    "megaphone": megaphone,
    "ai_voice": ai_voice,
    "dream_voice": dream_voice,
    "game_npc": game_npc,
    "capcut_pro_voice": capcut_pro_voice,
    "voice_speech": voice_speech,
}


def apply_preset(input_file, preset_name, output_file):
    board = VOICE_PRESETS[preset_name]

    with AudioFile(input_file) as f:
        audio = f.read(f.frames)
        sr = f.samplerate

    effected = board(audio, sr)
    effected = effected.T

    with AudioFile(output_file, "w", sr, effected.shape[1]) as f:
        f.write(effected)


stage_host_board1 = Pedalboard(
    [
        # ===== 麦克风频响模拟 =====
        HighpassFilter(cutoff_frequency_hz=90),  # 去舞台低频
        PeakFilter(cutoff_frequency_hz=2800, gain_db=4, q=0.9),  # 提高清晰度
        PeakFilter(cutoff_frequency_hz=180, gain_db=2, q=0.8),  # 轻微近讲感
        LowpassFilter(cutoff_frequency_hz=11000),  # 扩音系统高频衰减
        Distortion(drive_db=2),  # 模拟扩音系统染色
        # ===== 主压缩 =====
        Compressor(threshold_db=-18, ratio=4, attack_ms=4, release_ms=120),
        # ===== 舞台空间 =====
        Reverb(room_size=0.35, wet_level=0.25, dry_level=1.0, width=0.6, damping=0.6),
        # ===== 最终音量补偿 =====
        Gain(gain_db=3),
    ]
)
stage_host_board2 = Pedalboard(
    [
        # ===== 麦克风频响 =====
        HighpassFilter(90),
        PeakFilter(2800, 4, 0.9),
        PeakFilter(180, 2, 0.8),
        LowpassFilter(11000),
        # ===== 喷麦模拟 =====
        PeakFilter(140, 5, 0.7),
        PeakFilter(4500, 2, 1.2),
        Distortion(3),
        # ===== 主压缩 =====
        Compressor(threshold_db=-18, ratio=4, attack_ms=4, release_ms=120),
        # ===== 空间 =====
        Reverb(room_size=0.35, wet_level=0.25, width=0.6, damping=0.6),
        Gain(3),
    ]
)


stage_host_board = Pedalboard(
    [
        PeakFilter(160, 3, 0.8),
        PeakFilter(3000, 5, 1.0),
        HighpassFilter(85),
        LowpassFilter(11500),
        Distortion(3),
        Compressor(threshold_db=-20, ratio=5, attack_ms=3, release_ms=120),
        Mix(
            [
                # 干声
                Pedalboard([Gain(0)]),
                # 纯混响
                Pedalboard(
                    [
                        Reverb(
                            room_size=0.55,
                            wet_level=1.0,
                            dry_level=0.0,
                            damping=0.6,
                            width=0.7,
                        )
                    ]
                ),
                # 纯延迟
                Pedalboard([Delay(delay_seconds=0.12, feedback=0.25, mix=1.0)]),
            ]
        ),
        Gain(3),
    ]
)


def generate_preset_variants(input_wav):
    """
    根据预设参数批量生成不同风格的内心独白音效
    """
    input_filename = os.path.basename(input_wav).split(".")[0]

    with AudioFile(input_wav) as f:
        audio = f.read(f.frames)
        samplerate = f.samplerate

    # 定义 4 种风格的声学参数
    presets = {
        "1_Intimate": {  # 极度贴耳：几乎无回音，低语感强
            "delay_mix": 0.05,
            "room_size": 0.15,
            "wet_level": 0.10,
            "damping": 0.9,
            "chorus_mix": 0.05,
            "ratio": 3,
        },
        "2_Standard": {  # 标准独白：电视剧最常用的平衡感
            "delay_mix": 0.15,
            "room_size": 0.35,
            "wet_level": 0.25,
            "damping": 0.7,
            "chorus_mix": 0.12,
            "ratio": 4,
        },
        "3_Deep": {  # 深邃思索：余音缭绕，适合情感深沉的戏份
            "delay_mix": 0.22,
            "room_size": 0.50,
            "wet_level": 0.38,
            "damping": 0.4,
            "chorus_mix": 0.20,
            "ratio": 6,
        },
        "4_Ethereal": {  # 虚幻梦境：强烈的空间扩散，非现实感极强
            "delay_mix": 0.35,
            "room_size": 0.75,
            "wet_level": 0.55,
            "damping": 0.2,
            "chorus_mix": 0.40,
            "ratio": 8,
        },
    }

    print(f"🚀 开始批量处理：{input_filename}")

    for name, p in presets.items():
        # 构建专业音频处理链
        board = Pedalboard(
            [
                # 延迟器：模拟初次反射带来的重影
                Delay(delay_seconds=0.02, feedback=0.1, mix=p["delay_mix"]),
                # 混响器：营造空间感
                Reverb(
                    room_size=p["room_size"],
                    wet_level=p["wet_level"],
                    dry_level=1.0,  # 保持原声清晰
                    width=0.8 if name == "4_Ethereal" else 0.5,
                    damping=p["damping"],
                ),
                # 合唱器：增加声音厚度和主观质感
                Chorus(rate_hz=1.0, depth=0.3, mix=p["chorus_mix"]),
                # 压缩器：拉近声音细节
                Compressor(
                    threshold_db=-22, ratio=p["ratio"], attack_ms=5, release_ms=150
                ),
                # 增益：补偿音量
                Gain(gain_db=4),
            ]
        )

        # 执行处理并导出
        output_name = f"{input_filename}_{name}.wav"
        effected = stage_host_board(audio, samplerate)
        effected = effected.T

        print(effected.max())
        print(effected.min())
        print(effected.shape)
        with AudioFile(output_name, "w", samplerate, effected.shape[1]) as f:
            f.write(effected)
        print(f"✅ 已生成版本: {output_name}")


if __name__ == "__main__":
    # 指定你的音频文件路径
    target_file = "a.wav"

    if os.path.exists(target_file):
        # generate_preset_variants(target_file)
        apply_preset(target_file, "studio_clean", "a_studio_clean.wav")
        apply_preset(target_file, "stage_host", "a_stage_host.wav")
        apply_preset(target_file, "motivational", "a_motivational.wav")
        apply_preset(target_file, "inner_voice", "a_inner_voice.wav")
        apply_preset(target_file, "radio", "a_radio.wav")
        apply_preset(target_file, "cinematic", "a_cinematic.wav")
        apply_preset(target_file, "megaphone", "a_megaphone.wav")
        apply_preset(target_file, "ai_voice", "a_ai_voice.wav")
        apply_preset(target_file, "dream_voice", "a_dream_voice.wav")
        apply_preset(target_file, "game_npc", "a_game_npc.wav")
        apply_preset(target_file, "radio_voice", "a_radio_voice.wav")
        apply_preset(target_file, "capcut_pro_voice", "a_capcut_pro_voice.wav")
        apply_preset(target_file, "voice_speech", "a_voice_speech.wav")
    else:
        print("错误：文件路径不存在，请检查路径设置。")
