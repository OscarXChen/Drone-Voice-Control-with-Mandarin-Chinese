# -*- coding: utf-8 -*-
import paramiko
# 输入用户名、密码、ip等
ip = "10.42.0.1"
port =  22
user = "lj"
password = "123456"
#创建一个ssh对象
ssh = paramiko.SSHClient()
#自动选择yes
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 建立连接
ssh.connect(ip,port,user,password,timeout = 10)
#输入linux命令
#ssh.exec_command('cd pix;pwd')
#ssh.exec_command('pwd')
while True:
	#等待输入命令
    #temp = str(input("input:"))
    temp="python connect.py"
    print(temp)
    stdin,stdout,stderr = ssh.exec_command(temp)
    # 输出命令执行结果
    result = stdout.read()
    print(result)
    input("结束")
#关闭连接
ssh.close()