import requests
import _init_path
import feature
import time
import paramiko
#-------------------------SSH登录树莓派部分-------------------------
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
#-------------------------SSH登录树莓派部分结束-------------------------

#-------------------------端到端的语音识别部分-------------------------
from record import record
server = "http://localhost:5000/recognize"

for i in range(5):


    record("record.wav", time=3)
    f = open("record.wav", "rb")
    files = {"file": f}
    start_time=time.perf_counter()
    r = requests.post(server, files=files)
    end_time=time.perf_counter()
    print("")
    print("识别结果:")
    print(r.text)
    print("识别所花时间：{:.2f}s".format(end_time-start_time))
    if ("起飞" in r.text) or ("启动" in r.text) or ("开始" in r.text):
        print("发送 起飞 命令")
        temp="python arm.py"                            # arm.py用于让无人机起飞
        print(temp)
        stdin,stdout,stderr = ssh.exec_command(temp)    # 使用SSH执行运行arm.py命令
        result = stdout.read()                          # 输出命令执行结果
        print(result)
        input("本次命令发送结束")

    if ("连接" in r.text) or ("通讯" in r.text) or ("测试" in r.text):
        print("发送 连接 命令")
        temp="python connect.py"                            # connect.py用于测试和无人机的通讯
        print(temp)
        stdin,stdout,stderr = ssh.exec_command(temp)    # 使用SSH执行运行connect.py命令
        result = stdout.read()                          # 输出命令执行结果
        print(result)
        input("本次命令发送结束")

    if ("停止" in r.text) or ("停下" in r.text) or ("关机" in r.text) or ("停机" in r.text):
        print("发送 停机 命令")
        temp="python stop.py"                            # arm.py用于让无人机起飞
        print(temp)
        stdin,stdout,stderr = ssh.exec_command(temp)    # 使用SSH执行运行arm.py命令
        result = stdout.read()                          # 输出命令执行结果
        print(result)
        input("本次命令发送结束")

input("输入任意键结束程序\n")
