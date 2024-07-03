import subprocess

def execute_remote_script(username):

    # Путь к локальному скрипту на сервере
    script_path = '/home/konstantin/bot_VPN/scripts/create_ovpn_1_day.sh'

    result = subprocess.run([script_path, username], capture_output=True, text=True)

    if result.returncode == 0:
        # Если скрипт выполнен успешно, вернуть путь к сгенерированному файлу .ovpn
        return f'/tmp/{username}.ovpn', "Файл .ovpn успешно сгенерирован и загружен."
    else:
        # В случае ошибки, вернуть сообщение об ошибке
        error_message = result.stderr.strip()
        return None, f"Ошибка при выполнении скрипта на сервере: {error_message}"

# Пример использования
username = "kos"
ovpn_file_path, message = execute_remote_script(username)
if ovpn_file_path:
    print(f"Сгенерирован файл .ovpn: {ovpn_file_path}")
else:
    print(f"Ошибка: {message}")
