import paramiko

ip = '192.168.1.54'
username = 'david'
password = 'password123'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy)

client.connect(hostname=ip, username=username, password=password, look_for_keys=False)

stdin, stdout, stderr = client.exec_command('ls /home/david')
print(stdout.read())

client.close()