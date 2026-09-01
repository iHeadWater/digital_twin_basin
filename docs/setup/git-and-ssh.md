# git 与 ssh 配置

目标:配置好 ssh 密钥,用 ssh 方式克隆本仓库。全程约 20 分钟,只需做一次。

## 1. 安装 Git

- Windows:下载 [Git for Windows](https://git-scm.com/download/win),安装时全部默认选项即可
- macOS:`xcode-select --install` 或安装 [Homebrew 版](https://git-scm.com/download/mac)
- Linux:`sudo apt install git`(Ubuntu/Debian)

安装后打开 **Git Bash**(Windows)或终端(macOS/Linux),后续命令都在这里执行。

## 2. 首次配置(告诉 git 你是谁)

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

> 建议使用注册 GitHub 时的邮箱。

## 3. 生成 ssh 密钥

```bash
ssh-keygen -t ed25519 -C "你的邮箱"
```

一路回车(不设密码短语即可),生成在 `~/.ssh/id_ed25519`。

查看公钥内容:

```bash
cat ~/.ssh/id_ed25519.pub
```

复制输出的**整行**(以 `ssh-ed25519` 开头,以你的邮箱结尾)。

## 4. 把公钥添加到 GitHub

1. 登录 GitHub → 右上角头像 → **Settings**
2. 左侧 **SSH and GPG keys** → **New SSH key**
3. Title 随意(如"课程笔记本"),Key 粘贴刚才的整行 → **Add SSH key**

## 5. 测试连接

```bash
ssh -T git@github.com
```

- 首次连接询问是否继续:`yes` 回车
- 看到 `Hi <用户名>! You've successfully authenticated...` 即成功

## 6. 克隆本仓库

```bash
git clone git@github.com:iHeadWater/digital_twin_basin.git
cd digital_twin_basin
```

完成。之后每次上课前,进入仓库目录执行 `git pull` 即可拿到最新的演示代码与素材。

## 常见问题

**Q:校园网连不上 github.com 或速度极慢?**
> TODO(教师):确定学校/课程提供的解决方案(代理、镜像站等)后在此写明。

**Q:`ssh -T` 报 `Permission denied (publickey)`?**
- 公钥没复制完整,或没添加到 GitHub → 重新执行第 4 步
- 检查公私钥是否配对:重新 `cat ~/.ssh/id_ed25519.pub` 核对

**Q:克隆时报 `Host key verification failed`?**
- 执行 `ssh -T git@github.com` 时输入 `yes` 即可,这是首次连接的正常确认
