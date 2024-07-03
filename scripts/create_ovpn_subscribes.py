import subprocess
import os

def execute_remote_script(username, days):
    script_path = '/home/konstantin/bot_VPN/scripts/create_ovpn.sh'
    local_file_path = f'/home/konstantin/{username}.ovpn'

    try:
        # Выполнение локального скрипта
        result = subprocess.run(['bash', script_path, username, str(days)], check=True, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Script failed with return code {result.returncode}")

        if not os.path.exists(local_file_path):
            raise FileNotFoundError(f"File {local_file_path} not found after script execution")

        return local_file_path
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

