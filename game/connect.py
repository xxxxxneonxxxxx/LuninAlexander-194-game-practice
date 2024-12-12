import pymysql
import socket


def connect_to_database():
    try:
        connection = pymysql.connect(
            host="kosfaton.beget.tech",
            user="kosfaton_aleksl",
            password="WFDhjIOlM6P",
            database="kosfaton_aleksl",
            port=3306
        )

        print("Подключение к базе данных успешно!")
        return connection

    except pymysql.MySQLError as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

conn = connect_to_database()
if conn:
    conn.close()
