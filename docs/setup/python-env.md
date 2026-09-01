# python 环境搭建

目标:装好 miniconda,创建课程专用环境。全程约 30 分钟,只需做一次。

## 1. 安装 Miniconda

- Windows:下载 [Miniconda 安装器](https://docs.conda.io/en/latest/miniconda.html)(选 Python 3.x 的 64-bit 版),安装时勾选"Add to PATH"以外的默认项即可
- macOS / Linux:按官网命令行安装说明执行

Windows 用户之后请使用 **Anaconda Prompt(miniconda3)** 执行下列命令。

## 2. 创建课程环境

```bash
conda create -n dtb python=3.11 -y
conda activate dtb
```

`dtb`(digital twin basin)是课程环境名。以后每次打开新终端,先 `conda activate dtb`。

## 3. 安装课程基础库

```bash
conda install -c conda-forge numpy pandas matplotlib jupyterlab -y
```

> 后续各章 demo 若需要更多库(如 `torch`、`xarray`、`geopandas`),会在对应章节的 README 中写明,
> 并随 demo 提供一键安装的环境文件。

## 4. 验证环境

```bash
python -c "import numpy, pandas, matplotlib; print('环境就绪')"
```

输出 `环境就绪` 即完成。可以再执行 `jupyter lab` 熟悉一下 Notebook 界面(`Ctrl+C` 退出)。

## 常见问题

**Q:提示 `conda 不是内部或外部命令`?**
- Windows:改用开始菜单里的 **Anaconda Prompt(miniconda3)**,不必手动配 PATH

**Q:下载库很慢?**
> TODO(教师):确定推荐的镜像源(如清华 TUNA conda 镜像)配置命令后在此写明。

**Q:装错环境 / 环境乱了?**
- 删掉重来:`conda deactivate` → `conda remove -n dtb --all -y` → 从第 2 步重来
