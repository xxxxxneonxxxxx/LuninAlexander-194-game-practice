import pymysql

from serv.CRUDD import PRINT_TABLE_USERS
from serv.connect import connect_to_database


# CREATE (Добавление пользователя)
def add_user(name, password):
    conn = connect_to_database()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        query = "INSERT INTO users (user_name, user_password) VALUES (%s, %s)"
        cursor.execute(query, (name, password))
        conn.commit()
        print("Пользователь успешно добавлен.")
    except pymysql.MySQLError as e:
        print(f"Ошибка добавления пользователя: {e}")
    finally:
        cursor.close()
        conn.close()


# add_time (Добавление времени пользователя)
def add_time(name, time, col_strok):
    conn = connect_to_database()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        query = """
            INSERT INTO tablica (user_name, time,tip)
            VALUES (%s, %s, %s)
        """
        values = (
            name,
            time,
            col_strok
        )
        cursor.execute(query, values)
        conn.commit()
        print("Время пользователя успешно добавлено.")
    except pymysql.MySQLError as e:
        print(f"Ошибка добавления времени: {e}")
    finally:
        cursor.close()
        conn.close()


# UPDATE (Обновление времени)
def UPDATE_TIME(name, time, column_name):
    conn = connect_to_database()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        query = f"""
            UPDATE tablica
            SET {column_name} = %s
            WHERE user_name = %s
        """
        cursor.execute(query, (time, name))
        conn.commit()
        print(f"Время обновлено для {name}.")
    except pymysql.MySQLError as e:
        print(f"Ошибка обновления времени: {e}")
    finally:
        cursor.close()
        conn.close()


# READ_PROV (Проверка пользователя)
def READ_PROV(user_name, user_password):
    conn = connect_to_database()
    if not conn:
        return False
    cursor = conn.cursor()
    try:
        query = "SELECT * FROM users WHERE user_name = %s AND user_password = %s"
        cursor.execute(query, (user_name, user_password))
        result = cursor.fetchone()
        return bool(result)
    except pymysql.MySQLError as e:
        print(f"Ошибка проверки пользователя: {e}")
        return False
    finally:
        cursor.close()
        conn.close()


# SORT_READ (Сортировка по времени)
def SORT_READ():
    conn = connect_to_database()
    if not conn:
        return []
    cursor = conn.cursor()
    try:
        query = """
            SELECT user_name, time5X5, time5X6, time6X6, time6X7, time7X7, time8X7, time8X8
            FROM tablica
            ORDER BY time5X5 ASC
            LIMIT 10
        """
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except pymysql.MySQLError as e:
        print(f"Ошибка сортировки: {e}")
        return []
    finally:
        cursor.close()
        conn.close()
print(PRINT_TABLE_USERS())

# PRINT_TABLE_TIME (Вывод данных таблицы tablica)
def PRINT_TABLE_TIME():
    conn = connect_to_database()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        query = "SELECT * FROM tablica"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except pymysql.MySQLError as e:
        print(f"Ошибка вывода таблицы: {e}")
    finally:
        cursor.close()
        conn.close()


# PRINT_TABLE_USERS (Вывод данных таблицы users)
def PRINT_TABLE_USERS():
    conn = connect_to_database()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        query = "SELECT * FROM users"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except pymysql.MySQLError as e:
        print(f"Ошибка вывода таблицы: {e}")
    finally:
        cursor.close()
        conn.close()
PRINT_TABLE_TIME()
PRINT_TABLE_USERS()
