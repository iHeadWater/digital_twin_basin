# 第 3 讲 · 深度学习水文模型

> 本讲对应课堂 PPT：《深度学习水文模型》。PPT 讲原理与结构，这里给你课前读 + 动手练。

## 这一讲你会学到

- 把「降雨、气象条件、流域属性 → 未来流量」看作一个学习问题，说出模型的输入、输出与训练目标
- 理解神经网络为什么能表达复杂的降雨—径流关系
- 明白水文过程为什么有"时间依赖"，以及 RNN / LSTM 为什么为此而生
- 区分训练集 / 验证集 / 测试集，看懂"过拟合"
- 知道「大样本训练、跨流域泛化、预训练与微调」分别解决什么问题
- 会读一条过程线，会看 NSE、洪峰误差、峰现时间误差这几个评价指标
- 认识深度学习模型的边界：它在什么条件下可能失效

## 动手练（课后）

本讲的动手内容（跑通一个最小 LSTM，改改参数看结果变化）：

> 想先预习？公开数据集（如 CAMELS）与数据来源见 [data/README.md](../../data/README.md)；评价指标 NSE 的直觉可以在课后先查一查。

请前往[数字孪生流域课程作业](https://github.com/iHeadWater/digital_twin_watershed_homework),找到本章节对应的课程作业，并按作业说明完成练习。（注：本章具体作业存放在LSTM_camels_homework分支中。）  
补充：作业过程中用到的git的相关操作  
### 1. 下载作业仓库  
打开终端，进入准备存放作业的文件夹（自己建的），然后执行：  
```bash   
git clone https://github.com/iHeadWater/digital_twin_watershed_homework.git
cd digital_twin_watershed_homework
```
### 2.找到本章对应的作业  
获取并查看仓库中的全部分支：  
```bash
git fetch origin
git branch -a
```
在输出中找到：  
```text
remotes/origin/LSTM_camels_homework
```
### 3.切换到本章作业   
第一次进入该作业时执行：  
```bash
git switch -c LSTM_camels_homework origin/LSTM_camels_homework
```
检查当前分支：  
```bash
git branch --show-current
```
终端显示以下内容，说明已经进入正确的作业：  
```text
LSTM_camels_homework
```
### 4.按作业说明完成练习  
查看当前分支中的文件：  
```bash
ls
```
打开该分支中的`README.md`，按照其中的环境配置、数据准备和运行步骤完成练习。  
### 5.保存自己的修改  
完成一部分练习后，查看修改了哪些文件（注：不要直接使用`git add`，·先用`git status`检查一下，再添加本次确实需要保存的文件）：
```bash
git status
```
添加需要保存的文件：  
```
git add 文件名
```
保存本次修改记录：  
```bash
git commit -m "本次完成了xxx"
#记录自己的作业完成进度
```
查看提交记录：  
```bash
git log --oneline
```
### 再次继续作业  
以后重新打开终端时，进入本地仓库并切换到作业分支：
```bash
cd digital_twin_watershed_homework
git switch LSTM_camels_homework
git status
```
然后继续按照作业要求完成练习。


## 配套素材

本讲公开素材（LSTM 一页纸、NSE 指标说明等）正在补充中，就绪后列在这里。教师向的教学规划归档在 [docs/ideas/](../../docs/ideas/)，学生无需阅读。

## 学生反馈与迭代记录

| 日期 | 来源 | 反馈 | 处理 |
|---|---|---|---|
