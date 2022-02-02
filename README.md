# Drone-Voice-Control-with-Mandarin-Chinese
A project that using mandarin Chinese to control drones

这是一个致力于使用普通话的自然语音来控制无人机的本科毕设项目。

这是一个勉强可行的方案，项目事实上没有完全达到预期目标，但我认为尤其对本科生而言，我已完成的部分仍然有较好的参考价值。

将项目记录在此，希望可以帮到你。

项目的总体架构如下所示：

<img width="822" alt="github01_系统架构" src="https://user-images.githubusercontent.com/42312874/151939648-59e418a2-f387-46be-b7fd-784a89e3a556.png">

这个项目架构看着复杂，但是大多使用的是已有的开源架构，本项目核心工作量是两点：

1.位于PC上位机的语音识别程序
2.位于机载树莓派的无人机飞行指令程序

PC上位机和

1.语音识别程序
语音识别程序几乎完全基于这个项目开发，经过简单的再编写而得来：
使用了该项目作者的语音识别数据库
