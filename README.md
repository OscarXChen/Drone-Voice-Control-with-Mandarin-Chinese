# Drone-Voice-Control-with-Mandarin-Chinese
A project that using mandarin Chinese to control drones

这是一个致力于使用普通话的自然语音来控制无人机的本科毕设项目。

## 写在最前面

这是一个勉强可行的方案，项目事实上没有完全达到预期目标，仅是勉强完成项目要求。

但我认为已完成的部分，仍有较好的参考价值，尤其对尝试建立无人机系统的初学者或本科生，

将项目记录在此，希望可以帮到你。

---

## 0.概述

项目的总体架构如下所示：

<img width="822" alt="github01_系统架构" src="https://user-images.githubusercontent.com/42312874/151939648-59e418a2-f387-46be-b7fd-784a89e3a556.png">

这个项目架构看着复杂，但是大多使用的是已有的开源架构，本项目核心工作量是三点：

**1.运行于PC上位机的语音识别与无人机飞行指令程序**

**2.运行于机载树莓派上的无人机飞行控制程序**

**3.以恰当的方式搭建系统，使得语音识别程序和飞行指令程序得以协同工作**

尤其对于第2点，需要注意的是，本项目目前的实现程度为“通过语音指令，命令无人机运行已写好的不同的运动脚本”，其中已写好的运动脚本是不可时刻更改的，需要停机重新上传才能修改脚本。

即和“一般意义上的用语音控制无人机”的含义不同，是一种低配版的语音控制手段。但是本项目已建立了系统的数据连接，推测修改位于机载树莓派的运动脚本可以达到“一般意义上的用语音控制无人机”的目标。

---

## 1.语音识别程序

语音识别程序基于这个项目开发，语音识别算法部分使用的是[MASR](https://github.com/nobody132/masr)的deemo

事实上本项目完全可以采用其他的语音识别算法，语音识别和无人机飞行指令部分耦合性较低，使用MASR的主要原因是，这是一个

## 2.无人机飞行指令程序

无人机飞行指令程序基于[DroneKit](https://github.com/dronekit/dronekit-python)库开发，参考了[苍穹四轴](https://shop59774382.taobao.com/)的项目文件

## 3.系统协同

### 3.1 用户语音至PC上位机
蓝牙麦克风，一插就行，带个[Pyaudio](https://people.csail.mit.edu/hubert/pyaudio/)库就可以了
### 3.2 PC上位机中，自动语音转文本（ASR）与无人机控制程序
出于便携性的考虑（由于技术水平不够），无人机飞行指令程序写在了自动语音转文本的程序下面，即当语音转换为文本后，提取文本中的部分有关飞行指令的术语，准备将其发送给树莓派执行，目前做到的是这一部分的系统协同也没有问题
### 3.3 PC上位机的语音识别与无人机飞行指令程序至树莓派上的飞行控制程序
这两个程序的通信主要是通过SSH登录实现的

组网：PC连接树莓派上的热点进行组网，当然也可以用其他方式

调试：PC开了一个Ubuntu的虚拟机便于SSH调试，当然也可以用其他方式

自动化通信：主要通过[Paramiko](https://github.com/paramiko/paramiko)库进行，具体实现请看[这里](https://github.com/OscarXChen/Drone-Voice-Control-with-Mandarin-Chinese/tree/main/%E8%AF%AD%E9%9F%B3%E8%AF%86%E5%88%AB%E7%A8%8B%E5%BA%8F/%E7%A8%8B%E5%BA%8F%E6%BA%90%E7%A0%81)的“树莓派test.py”文件

执行：SSH登陆后，执行已写好的命令，如[这里](https://github.com/OscarXChen/Drone-Voice-Control-with-Mandarin-Chinese/tree/main/%E6%97%A0%E4%BA%BA%E6%9C%BA%E6%8E%A7%E5%88%B6%E7%A8%8B%E5%BA%8F)的命令

### 3.4 树莓派上的飞行控制程序至飞控Pixhawk
使用已有的成熟接线方法，比如[这个](https://mp.weixin.qq.com/s?__biz=MzkyNzI1MDUyNw==&mid=2247484996&idx=1&sn=4028c5c1c6a0beab55587ae8535b6d58&source=41#wechat_redirect)，当然也可以用其他方式进行接线

--- 
以上，希望可以帮到你

自述文档未来会继续更新,添加更多细节 当前版本为：1.7
