import pymysql



def connect_to_database():
    try:
        connection = pymysql.connect(
            host="-",
            user="-",
            password="-",
            database="-",
            port='-'
        )
        return connection

    except pymysql.MySQLError as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

conn = connect_to_database()
if conn:
    conn.close()
