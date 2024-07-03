import subprocess
import os
from dotenv import load_dotenv
import paramiko

dotenv_path = '/.env'
load_dotenv(dotenv_path)

SSH_HOST = os.getenv('SSH_HOST')
SSH_USER = os.getenv('SSH_USER')
SSH_PRIVATE_KEY = os.getenv('SSH_PRIVATE_KEY')

def execute_remote_script(username, day):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=SSH_HOST, username=SSH_USER, key_filename=SSH_PRIVATE_KEY)

    remote_script_path = '/home/konstantin/bot_VPN/scripts/create_ovpn.sh'
    build_command = f'sudo -S {remote_script_path} {username} {day}'

    stdin, stdout, stderr = client.exec_command(build_command)
    stdout.channel.recv_exit_status()

    client.close()

    return stdout.read().decode('utf-8')

# Пример использования функции
result = execute_remote_script('kos', day=1)
print(result)