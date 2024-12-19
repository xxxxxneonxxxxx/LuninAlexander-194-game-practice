import pymysql

from connect import connect_to_database

def add_user(name, password):
    conn = connect_to_database()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        query = "INSERT INTO users (user_name, user_password) VALUES (%s, %s)"
        cursor.execute(query, (name, password))
        conn.commit()
        return True
    except pymysql.MySQLError as e:
        return False
    finally:
        cursor.close()
        conn.close()

def add_time(name, time, col_strok):
    print(name, time, col_strok)
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
        return True
    except pymysql.MySQLError as e:
        return False
    finally:
        cursor.close()
        conn.close()

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

def SORT_TIME(tip):
    conn = connect_to_database()
    if not conn:
        print("Не удалось подключиться к базе данных.")
        return {}

    cursor = conn.cursor()
    try:
        print(f"Ищем записи с типом: {tip}")

        query = """
            SELECT user_name, time, tip
            FROM tablica
            WHERE tip = %s
            ORDER BY time ASC
            LIMIT 10
        """
        cursor.execute(query, (tip,))

        results = cursor.fetchall()
        print(f"Результаты запроса: {results}")

        response = {}

        for index, record in enumerate(results, start=1):
            response[record[0]] =  str(record[1]),

        print(f"Обработанный словарь: {response}")
        return response
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return {}
    finally:
        cursor.close()
        conn.close()


def PRINT_TABLE_TIME():
    conn = connect_to_database()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        query = "SELECT * FROM tablica"
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except pymysql.MySQLError as e:
        print(f"Ошибка вывода таблицы: {e}")
    finally:
        cursor.close()
        conn.close()

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
print(SORT_TIME("5X5"))
print(PRINT_TABLE_TIME())
