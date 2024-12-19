import json
import socket


def input_us(zapros):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(('server.pbtusur.ru', 12331))
            print("Подключение к серверу установлено.")

            json_message = json.dumps(zapros)
            client_socket.sendall(json_message.encode('utf-8'))
            print("Сообщение отправлено серверу.")

            received_data = client_socket.recv(1024)
            json_data = received_data.decode('utf-8')

            try:
                data = json.loads(json_data)
                print("Ответ от сервера:", data)
                return data
            except json.JSONDecodeError as e:
                print(f"Ошибка декодирования JSON: {e}")
                return None
    except Exception as e:
        print(f"Ошибка при подключении или обработке данных: {e}")
        return None
