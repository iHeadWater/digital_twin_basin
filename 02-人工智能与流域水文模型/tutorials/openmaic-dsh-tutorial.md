# 第 2 讲配套实操 · 从配好一个大模型，到让你的 Agent 生成一节课

> 状态：工作稿（2026-09）。OpenMAIC / DSH / dsh-openmaic 都在快速迭代，正文命令以**官方 README 为准**；若某条跑不通，先看文末「常见坑」，再把报错原样贴给你的 Agent。
>
> 与教师素材规范的区分：本教程是**学生动手学 OpenMAIC**；把 AI 生成的课件**收进仓库各讲次 `materials/`** 的约定见 `02-人工智能与流域水文模型/materials/openmaic-workflow.md`（教师向）。

---

## 0. 这篇教程带给你什么

完成它，你会**亲手指挥一个 AI Agent 生成一节真正的课**——不是聊天式地"生成一段文字"，而是让它调用一个真实应用（OpenMAIC）产出一节可播放、可导出 PPT 的互动课件。这正好接住第 2 讲 PPT 的话头：**大模型不只会聊天，它能调用工具、完成真实任务**。

- 时间：约 90–120 分钟（课后 / 自选进度，不必一节课做完）
- 前置：本仓库已 clone、git 与 python 环境就绪（见 [docs/setup](../../docs/setup/)）
- 一句话地图：**npm（装工具）→ DSH（Agent 工作台）→ OpenMAIC（被调用的应用）→ 三者都在配同一套模型字段**

学完你手里会有两样东西：

1. 一节自己在 DSH 里指挥 agent 生成的**水文互动课件**（可播放 / 可导出 .pptx）；
2. 一张**"配置密码表"**——以后装任何 AI 工具，你都能看懂它要你填的那几项是什么。

---

## 1. 名词与背景，一次讲清

这一节是全文的记忆锚点。后面每一处"填一个 key / 一个地址"，都在回这里。

### 1.1 npm 是什么：装工具的"商店"

写好的程序（DSH、OpenMAIC 依赖的库……）通常打包成一个"包"放在仓库里，**npm** 就是帮你下载、安装、升级这些包的工具。你只需要会三句：

```bash
npm install -g <包名>    # 全局安装一个命令行工具（-g = global，装到系统里到处能用）
npm view <包名> version  # 看这个包的最新版本
npm config get registry  # 看当前从哪个"源"下载
```

npm 装的东西默认放在 `node_modules/`；`-g` 装在系统目录，于是多了一个能在任意终端直接敲的命令（比如装完 DSH 后，敲 `dsh` 就能用）。

### 1.2 国内没梯子怎么办：换一个"镜像源"

npm 默认去国外的官方源下载，国内经常很慢甚至失败。解决方法是换到**国内镜像**（npmmirror，淘宝 npm 镜像），内容实时同步：

```bash
npm config set registry https://registry.npmmirror.com
npm config get registry   # 应显示 registry.npmmirror.com
```

> 这不是 Linux 专用操作，Windows / Mac 命令完全一样。后面凡是 `npm ...` / `npx ...` / `pnpm ...` 下载慢，都先确认这一步已做。

### 1.3 大模型 API 的"四件套"

任何工具要调用大模型，都要告诉它四个信息。想象去一家很远的图书馆借书：

| 配置项 | 通俗理解 | 例子（DeepSeek） |
|---|---|---|
| **API Key** | 你的"读者证 / 钥匙"，证明你有权限调用 | `sk-...` |
| **Base URL（Base url）** | 图书馆的"门牌地址"，请求发去哪 | `https://api.deepseek.com` |
| **模型名（model）** | 你要借的"那本书/那个房间" | `deepseek-v4-flash` |
| **协议 / Provider** | 你和图书馆讲的"通用语言"（现在基本都是 OpenAI 兼容协议）；Provider = 谁家开的 | `openai-completions` / `deepseek` |

**Provider** 就是"模型厂商/入口"的代号：DeepSeek、OpenAI、硅基流动……都算一个 provider。很多工具用 `provider:model` 的写法，例如 OpenMAIC 里 `DEFAULT_MODEL=deepseek:deepseek-v4-flash` 表示"用 deepseek 这家提供的 deepseek-v4-flash 模型"。

### 1.4 同一个模型，可以有多个"入口"

同一个模型，可以走 DeepSeek 官方、也可以走硅基流动这类聚合平台。**区别只在 Base URL 和 Key**——所以配置时 key 和地址必须**配对**（用 A 家的 key 去请求 B 家的地址会报 401/认证错）。本教程统一用 DeepSeek 官方，避开这个坑。

### 1.5 DSH 与 OpenMAIC：谁是谁

- **DSH（DeepSeek Harness）**：一个 **Agent 工作台 / 运行时**，DeepSeek 出品，"万物皆插件"。你在这类工具里用自然语言布置任务，它能读文件、跑命令、装插件扩能力。跟 Claude Code、Codex 是同一族。
- **OpenMAIC**：清华 THU-MAIC 开源的**互动课堂生成应用**——给它一个主题或文档，它用多智能体协作生成"大纲→场景"，AI 老师讲解、可随堂测、可导出 PPT/HTML。它本身是一个**网页应用**，同时也提供可被 Agent 调用的能力。
- 本教程让两者通过 **dsh-openmaic 插件**连起来：你在 DSH 里说"生成一节课"，DSH 帮你去调本机的 OpenMAIC。

### 1.6 pnpm 是什么（一句话）

OpenMAIC 项目用 **pnpm** 来装依赖（pnpm 是 npm 的同类、更快更省空间）。用 npm 装一次即可：`npm install -g pnpm`。装完它读的源和 npm 一致（上面已换镜像）。

---

## 2. 环境准备（Windows / Mac 双轨 · 国内镜像）

### 2.1 装 Node.js（自带 npm）

要求 **Node.js ≥ 22**（OpenMAIC 要求 ≥22.19，建议直接装当前 LTS）。

- **Windows**：去官网下载 `.msi` 安装包，一路下一步 → <https://nodejs.org/en/download>
- **macOS**：官网下载 `.pkg` 安装；或用 Homebrew：`brew install node`
- 装完**新开一个终端**（让它读到新 PATH），自检：

```bash
node -v     # 应显示 v22 或更高
npm -v
```

> 若之前装过很旧的 Node：直接重新下载覆盖安装即可；不用管系统里残留的旧版。

### 2.2 换国内镜像 + 装 pnpm

```bash
npm config set registry https://registry.npmmirror.com
npm config get registry                 # 自检：显示 npmmirror
npm install -g pnpm
pnpm config get registry                # pnpm 也应显示 npmmirror
```

**检查点**：`npm -v`、`pnpm -v` 都能输出版本号，且 registry 是 npmmirror。

### 2.3 准备一个 DeepSeek 官方 API Key

教程下面需要"配模型"。统一用 **DeepSeek 官方**（本教程已按它配好所有示例，最省事）：

1. 打开 <https://platform.deepseek.com/> 注册登录；
2. 左侧 **API Keys** → **Create new API key** → 创建后**立刻复制保存**（只显示一次，丢了要重建）；
3. 到 **充值** 页充一点钱（支付宝/微信都行，几块钱就够本教程用）；
4. 记下你的模型名——在模型列表/官方文档看当前可用的，例如 `deepseek-v4-flash`。Base URL 用默认 `https://api.deepseek.com`。

> 提示：DeepSeek 目前主力是 `deepseek-v4-flash`（快、便宜）和 `deepseek-v4-pro`（更强），还有能看图片的多模态模型。教程生成课件用文本/推理即可，**统一填 `deepseek-v4-flash` 就基本不会错**；以你平台上实际能选的为准。

---

## 3. DSH 上手（前半场）

> 目标：装好 DSH、配好一个模型、让它在终端里答你一句话。跑通即过关。

### 3.1 安装

```bash
npm install -g @deepseek-ai/dsh
dsh --version      # 应输出版本号（当前约 0.1.x，还在快速迭代）
```

> 包名：`@deepseek-ai/dsh`（DeepSeek 官方）。若安装慢，确认 2.2 的镜像已配好。

### 3.2 启动并配置模型

运行：

```bash
dsh web
```

启动后浏览器打开 <http://localhost:3080>（DSH 是网页界面，不是纯命令行）。

首次使用进 **设置 → 模型（Settings → Models）→ 添加自定义提供方（Add a custom provider）**，把"四件套"填进去：

| 界面字段 | 填什么（DeepSeek 官方） |
|---|---|
| Provider ID | `deepseek`（小写，以后都引用它） |
| 显示名称 | `DeepSeek` |
| Base URL | `https://api.deepseek.com` |
| API 协议 | `openai-completions` |
| API 密钥 | 2.3 里创建的 `sk-...` |
| 模型 | 填 `deepseek-v4-flash`（可点「获取可用模型」试拉列表） |

**每个字段在配什么，对应 1.3 那张表**：Provider ID=给这家起个代号；Base URL=门牌；Key=钥匙；模型名=房间；协议=通用语言。保存后，把该 provider 设为**默认模型**（新会话默认用）。

### 3.3 验证

在 DSH 对话框里随便问一句：

> 请计算 23×17 等于多少，并把算式和结果一起列出来。

看到它正常回答即**过关**。（可选升级：给它一个本仓库的小任务，比如"读一下 README.md 前 20 行，告诉我这个课程仓库讲什么"——它会真的去读文件，这就是"Agent 能操作文件"的最初体验。）

**常见坑**：

| 现象 | 原因 / 处理 |
|---|---|
| 打不开 localhost:3080 | 确认 `dsh web` 那个终端还开着；端口被占就换（看 DSH 提示） |
| 报 401 / auth error | key 与 Base URL 不配对（1.4）；或 key 复制漏了字符 |
| 报 model not found | 模型名填错/该入口没有这个模型；到模型列表核对 |
| 很慢/连不上 | 你填的 Base URL 需要梯子——DeepSeek 官方国内可直连，确认 Base URL 没写错 |

> 伏笔：DSH 里能**装插件 = 给 agent 加能力**。下一节 OpenMAIC 就是被"装成插件"调用的。这个概念在第 4 讲会正式展开（Skill / MCP / 工具）。

---

## 4. 源码装 OpenMAIC（后半场）

> 目标：本机把 OpenMAIC 跑起来（浏览器能打开它的网页并生成一版课）。**不用 Docker**，纯源码 + pnpm。

### 4.1 clone 到仓库外

**不要** clone 进本课程仓库（它是课件/作业仓库，别污染）。在你想放代码的地方新建目录并 clone：

```bash
cd ~            # 或你自己放代码的目录
git clone https://github.com/THU-MAIC/OpenMAIC.git
cd OpenMAIC
```

国内访问 GitHub 慢的替代：

- 从 GitHub 网页点 **Code → Download ZIP** 下载解压（同样放到仓库外）；
- 或搜该仓库在 **GitCode / Gitee** 上的镜像地址 clone（以你能访问到的为准）。

### 4.2 装依赖（首次较久，属正常）

```bash
pnpm install
```

> 需要 Node ≥22.19、pnpm ≥10（第 2 节已备好）。这一步会下载大量依赖，几分钟到十几分钟都正常；中途断了重跑即可（pnpm 有缓存，续传很快）。

### 4.3 配模型（OpenMAIC 也要一份"四件套"）

```bash
cp .env.example .env.local
```

用文本编辑器打开 `.env.local`，找到这几行，**只填你要用的那个 provider**（以 DeepSeek 为例）：

```bash
DEEPSEEK_API_KEY=sk-你的key
# DEEPSEEK_BASE_URL=            # 用官方默认可留空；走其它入口就填那家的地址
# DEEPSEEK_MODELS=deepseek-v4-flash,deepseek-v4-pro  # 可选：显式列出可用模型
DEFAULT_MODEL=deepseek:deepseek-v4-flash
```

> 这里就是 1.3 的"四件套"**在文件里再出现一次**：前缀 `DEEPSEEK_` 是给哪个 provider、`_API_KEY` 是钥匙、`DEFAULT_MODEL` 里 `deepseek:` 指 provider、冒号后是模型名。DSH 在网页里填、OpenMAIC 在 `.env.local` 里填——**工具不同，概念同一套**。
>
> `DEEPSEEK_API_KEY` 填 2.3 里那个 `sk-...`；`DEEPSEEK_BASE_URL` 留空即用 DeepSeek 官方默认地址。
>
> 用 `DEEPSEEK_MODELS` 显式列模型有助于界面下拉可选；不填也常能自动发现，若生成时报 unknown model 再回来补这行。

### 4.4 启动并自检

```bash
pnpm dev
```

看到类似 `ready ... http://localhost:3000` 后，浏览器打开 <http://localhost:3000>，并顺手验证健康接口：

```bash
curl http://localhost:3000/api/health   # 或浏览器直接开这个地址
```

**检查点**：页面能打开，且 `/api/health` 有正常返回。

### 4.5 先"眼见为实"：在网页里生成一版

不急着上 DSH。先在 OpenMAIC 网页首页输入一个水文主题，例如：

> 用 30 分钟给没有水文背景的同学，讲清一个小流域的"降雨 → 径流"过程，配一张概念示意。

点生成，看它走 **大纲 → 场景** 两阶段，产出 AI 老师讲解的互动课堂。能生成出来，说明你的模型 key 配对了——**这是后半场的第一个胜利**。

**常见坑**：

| 现象 | 原因 / 处理 |
|---|---|
| `pnpm install` 报 node 版本不符 | Node 不够 22.19，重装 LTS（2.1） |
| 起服务报缺 key / model 校验失败 | `.env.local` 没填对 provider，或 `DEFAULT_MODEL` 格式错（应是 `provider:model`）；启动日志会点名缺哪个 |
| 生成时一直失败/报模型错 | 回 4.3 核对 provider 前缀与模型名；换 DeepSeek 官方入口最稳 |
| 端口 3000 被占 | 关掉占用程序，或按项目说明换端口 |

---

## 5. 用 dsh-openmaic 插件：让 Agent 驱动本地 OpenMAIC（主验收）

> 目标：回到 DSH，让它调用你刚装好的 OpenMAIC 生成那节水文课——**这是本教程的成品验收**。

### 5.1 给 DSH 装 OpenMAIC 插件

确保 OpenMAIC 的 `pnpm dev` 还在跑、DSH 已配置好模型。然后（在另一个终端）：

```bash
dsh plugin --profile web add git+https://github.com/THU-MAIC/dsh-openmaic.git
```

装完**重启 `dsh web`**（关掉再 `dsh web`），刷新浏览器。插件会注册几个工具（`openmaic_generate` 等）和一个教学 skill。

### 5.2 把插件指向"本地"而不是官方云

dsh-openmaic 默认把生成请求发给**官方云端 open.maic.chat**（此时无需访问码即可体验）。我们想让 agent 调用**自己装的那台**：在 DSH 的插件配置里，把该插件的 **`baseUrl` 改为 `http://localhost:3000`**（对应 OpenMAIC dev 服务地址）。`accessCode` 本地部署留空。

> 这正是 1.4 说的"同一个应用，多个入口"：官方云 / 本地实例，改一个地址就切换。若你暂时没把 OpenMAIC 跑起来，也可以先不改 baseUrl、直接用官方云体验一次全流程——两者都算过关。

### 5.3 指挥 DSH 生成一节课

在 DSH 对话框里说一句（可整句复制）：

> 请用 OpenMAIC 帮我生成一节中文互动课：给没有水文背景的同学讲清"小流域里降雨是怎么变成河道径流的"，尽量包含一张示意图和一个随堂小测。

DSH 的 agent 会判断该用 `openmaic_generate` 工具、带好参数提交给（本地）OpenMAIC，然后轮询等待异步生成。

- 课堂生成**较慢**（可能几分钟），属正常；若插件支持调 `pollInterval`，设大些（如 60000ms）更友好。
- 生成完成后，DSH 会给你一个**可播放课堂的链接**。

### 5.4 验收

- [ ] DSH 返回了一个 OpenMAIC 课堂链接，点开能播放（有 AI 老师讲解/页面）；
- [ ] 在 OpenMAIC（localhost:3000）里打开那节课，能**导出 .pptx**（可编辑幻灯片）或 **.html**（可离线播放）。

导出成功 = **本教程达成**。

### 5.5 一句话认识另外三个工具（非必须）

插件还注册了 `openmaic_slide` / `openmaic_widget` / `openmaic_render`：它们让 agent **在对话里就地渲染**单页幻灯片、交互小部件（模拟/游戏/代码）、HTML 教学卡片——不需要走整课生成，适合小片段的即时演示。想体验可以问 DSH：

> 用 openmaic 给我渲染一张能说明"蒸散发"概念的小卡片。

**常见坑**：

| 现象 | 原因 / 处理 |
|---|---|
| 插件找不到 / 工具不出现 | 装完没重启 `dsh web`；或 DSH 版本与插件要求不匹配（插件很新） |
| agent 说连不上 OpenMAIC | OpenMAIC `pnpm dev` 没在跑，或 baseUrl 指错（应为 localhost:3000） |
| generate 一直"生成中" | 大课堂本来就慢；把轮询间隔调大；看 OpenMAIC 终端有无报错 |
| 想直接用官方云试试 | 把 baseUrl 留默认 open.maic.chat（当前免访问码） |

---

## 6. 收尾 · 复盘三问

1. **回到 PPT**：第 2 讲说"大模型从语言走向任务执行"。这次你让 agent 干成的"真事"是什么？它和"让 AI 写一段话"差在哪？
2. **"配模型"为什么是通用技能**？DSH、OpenMAIC、以后任何 AI 工具，翻来覆去就是 key / base url / 模型名 / provider 这四样。会配一次，就会配全部。
3. **预告第 4 讲**：这里 DSH 是"装了个插件让 agent 会用 OpenMAIC"。第 4 讲会把这套拆开讲透——Skill 怎么沉淀方法、工具/API 怎么连接数据与模型、工作流怎么组织多步任务。你现在体会到的，就是那节课的引子。

最后：本教程与**作业无关**（作业在独立仓库实施）。做出来的课件不用交，是你自己的作品；想分享到课程共建，可提 issue 或在课上展示。

---

## 附：给教师的备注（不在正文出现）

- 教程有意**不含 Docker/云部署/运维**；OpenMAIC 用源码 + pnpm 起本地 dev 服务即可满足生成课件。
- 全教程统一用 **DeepSeek 官方** API（key 见 2.3），正文不再提校内网关等其它入口。
- `dsh-openmaic`、DSH、OpenMAIC 三方均快速迭代：正式上课前请按本教程**完整跑通一遍**（DeepSeek 官方 key），把命令、字段名、版本号按当时最新 README 校正一次，再发给学生。
