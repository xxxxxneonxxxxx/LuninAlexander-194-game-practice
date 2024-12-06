from datetime import datetime
from connect import connect_to_database
import pymysql


# Подключение
conn = connect_to_database()
if not conn:
    exit()

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    user_password INT NOT NULL
);
""")
print("Таблица 'users' создана.")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tablica (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    time TIME NOT NULL,
    tip VARCHAR(255) NOT NULL
);
""")
print("Таблица 'tablica' создана.")

users = [
    ("user1", 12345),
    ("user2", 23456),
    ("user3", 34567),
    ("user4", 45678),
    ("user5", 56789),
    ("user6", 67890),
    ("user7", 78901),
    ("user8", 89012),
    ("user9", 90123),
    ("user10", 1234)
]

current_time = datetime.now().strftime("0:%M:%S")
times = [
    ("user1", current_time, "type1"),
    ("user2", current_time, "type2"),
    ("user3", current_time, "type3"),
    ("user4", current_time, "type4"),
    ("user5", current_time, "type5"),
    ("user6", current_time, "type6"),
    ("user7", current_time, "type7"),
    ("user8", current_time, "type8"),
    ("user9", current_time, "type9"),
    ("user10", current_time, "type10")
]

# Вставка данных в таблицу users
for user_name, user_password in users:
    cursor.execute("""
        INSERT INTO users (user_name, user_password)
        VALUES (%s, %s)
    """, (user_name, user_password))
print("Данные добавлены в таблицу 'users'.")

# Вставка данных в таблицу tablica
for user_data in times:
    cursor.execute("""
        INSERT INTO tablica (user_name, time, tip)
        VALUES (%s, %s, %s)
    """, user_data)
print("Данные добавлены в таблицу 'tablica'.")

conn.commit()
cursor.close()
conn.close()

print("10 пользователей добавлены в таблицы 'users' и 'tablica'.")
