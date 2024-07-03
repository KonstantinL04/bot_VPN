import sqlite3
from datetime import datetime, timedelta

db_path = 'DB/user.db'

def is_key_active(date_received, days_valid=1):
    date_format = '%Y-%m-%d %H:%M:%S'
    received_date = datetime.strptime(date_received, date_format)
    if datetime.now() - received_date < timedelta(days=days_valid):
        return True
    return False

import sqlite3
from datetime import datetime, timedelta
from scripts.create_ovpn_subscribes import execute_remote_script

db_path = 'DB/user.db'

def is_key_active(date_received, days_valid=1):
    date_format = '%Y-%m-%d %H:%M:%S'
    received_date = datetime.strptime(date_received, date_format)
    if datetime.now() - received_date < timedelta(days=days_valid):
        return True
    return False

def get_key(username, key_type):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('SELECT date_received FROM users WHERE username = ? AND key_type = ?', (username, key_type))
    result = cursor.fetchone()
    
    if result:
        if is_key_active(result[0]):
            message = "Вы уже получали этот ключ ранее, и он все еще активен."
            file_path = None
        else:
            message = "Вы уже получали ключ ранее и его срок истек. Теперь вы можете только купить платную версию."
            file_path = None
    else:
        cursor.execute('INSERT OR REPLACE INTO users (username, key_type, date_received) VALUES (?, ?, ?)', 
                       (username, key_type, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        message = "Ваш тестовый ключ сгенерирован."
        file_path = execute_remote_script(username, 1)  # Генерация нового файла .ovpn
    
    conn.close()
    return message, file_path

