import paramiko

def ssh_connect(ip, port, user_name, passwd, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, user_name, passwd)

    stdin, stdout, stderr = ssh.exec_command(cmd)

    print(stdout.read().decode('utf-8'))
    print(stderr.read().decode('utf-8'))
    ssh.close()