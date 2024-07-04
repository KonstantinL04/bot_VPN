import subprocess
import os

def execute_remote_script(username, days):
    script_path = '/home/konstantin/bot_VPN/scripts/create_ovpn.sh'
    local_file_path = f'/home/konstantin/{username}.ovpn'

    try:
        # Выполнение локального скрипта
        result = subprocess.run(['bash', script_path, username, str(days)], check=True, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Ошибка скрипта с возвращаемым кодом {result.returncode}")

        if not os.path.exists(local_file_path):
            raise FileNotFoundError(f"Файл {local_file_path}не найден после выполнения скрипта")

        return local_file_path
    except Exception as e:
        print(f"Произошла ошибка {str(e)}")
        return None
