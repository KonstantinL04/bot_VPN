import subprocess

def execute_remote_script(username, days):
    # Путь к локальному скрипту на сервере
    script_path = '/home/konstantin/bot_VPN/scripts/create_ovpn.sh'

    result = subprocess.run([script_path, username, str(days)], capture_output=True, text=True)

    if result.returncode == 0:
        # Если скрипт выполнен успешно, вернуть путь к сгенерированному файлу .ovpn
        return f'/home/konstantin/{username}.ovpn', "Файл .ovpn успешно сгенерирован и загружен."
    else:
        # В случае ошибки, вернуть сообщение об ошибке
        error_message = result.stderr.strip()
        return None, f"Ошибка при выполнении скрипта на сервере: {error_message}"

# Пример использования функции
# ovpn_file_path, message = execute_remote_script("kos3", 3)
# if ovpn_file_path:
#     print(f"Путь к сгенерированному файлу .ovpn: {ovpn_file_path}")
# else:
#     print(f"Ошибка: {message}")