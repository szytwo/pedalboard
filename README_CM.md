## fork

https://github.com/spotify/pedalboard

## 安装

```
python -m venv venv
venv\Scripts\activate

pip install pedalboard -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install pydub scipy librosa tqdm


nvidia-smi -L  # 查看GUID

```

## GIT

```
git pull # 拉取
git push # 推送

git branch -r # 查看分支
git branch -m master # 重命名分支
git branch --set-upstream-to=origin/master master #关联远程分支origin/master 

git remote -v # 查看远程仓库
git remote remove origin # 移除远程仓库连接，origin，upstream

# 添加新的远程仓库，origin，upstream
git remote add upstream https://github.com/spotify/pedalboard.git

git fetch upstream # 从远程仓库拉取更新，origin，upstream
git checkout master # 切换到主分支
git merge upstream/master # 合并到本地分支,主分支名称可能是 ，origin，upstream，master,main 

git reset --hard origin/master # 强制覆盖本地代码

```