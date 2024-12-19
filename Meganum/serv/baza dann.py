from datetime import datetime
from connect import connect_to_database
import pymysql
from CRUDD import *
conn = connect_to_database()
if not conn:
    exit()

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    user_password VARCHAR(255) NOT NULL
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
    ("user1", current_time, "5X5"),
    ("user2", current_time, "5X6"),
    ("user3", current_time, "6X6"),
    ("user4", current_time, "6X7"),
    ("user5", current_time, "7X7"),
    ("user6", current_time, "7X8"),
    ("user7", current_time, "8X8"),
]

for user_name, user_password in users:
    cursor.execute("""
        INSERT INTO users (user_name, user_password)
        VALUES (%s, %s)
    """, (user_name, user_password))
print("Данные добавлены в таблицу 'users'.")

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
print(PRINT_TABLE_TIME())
print(PRINT_TABLE_USERS())