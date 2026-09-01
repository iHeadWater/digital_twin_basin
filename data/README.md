# 数据策略

本仓库**只收录可公开获取的数据**;大体积数据不进 git,由各章 demo 的下载脚本按需获取。
本文件是全仓库的数据总台账。

## 公开数据源清单

| 数据源 | 内容 | 服务的章节 | 获取方式 | 条款要点 |
|---|---|---|---|---|
| [CAMELS](https://camels.dartmouth.edu/) | 美国 671 个流域:气象强迫 + 逐日径流 + 流域属性 | ch02 模型、ch05 案例 | 官方站点打包下载 | 公开科研数据,使用需引用 |
| [ERA5 / ERA5-Land](https://cds.climate.copernicus.eu/) | 再分析气象强迫(降水、气温等) | ch02、ch03 | Copernicus CDS,需注册 | Copernicus 许可 |
| DEM(SRTM / Copernicus) | 数字高程 | ch03、ch05 | [OpenTopography](https://opentopography.org/) / USGS Earth Explorer | 公开 |
| [GPM IMERG](https://disc.gsfc.nasa.gov/) | 卫星遥感降水 | ch04 监测 | NASA GES DISC,需注册 | NASA 数据政策 |
| [GRDC](https://grdc.bafg.de/) | 全球河流径流观测 | ch04、ch05 | 官方站点申请 | 公开,需引用 |

> TODO(教师):随各章 demos 落地,补充精确数据版本、对应下载脚本名与标准引用格式(BibTeX)。

## 下载产物目录

`data/downloads/` 已被 `.gitignore` 忽略——所有脚本下载的数据放这里。
换机器 / 删掉后重跑下载脚本即可,不进仓库。

## 红线:内部数据不进仓库

课程涉及的内部流域数据(如松辽流域相关数据)**不进入本仓库**。如需在演示中使用:

1. 放在本机**仓库外**的本地目录
2. demo 通过配置文件 / 环境变量指向该本地路径
3. 仓库中只记录"需要什么数据、什么格式"的说明,不记录数据本身
