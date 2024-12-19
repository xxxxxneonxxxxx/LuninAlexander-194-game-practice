import socket
import json

def output_us(client_message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(('server.pbtusur.ru', 12331))
            print("Подключение к серверу установлено.")
            json_message = json.dumps(client_message)
            client_socket.sendall(json_message.encode('utf-8'))
            print("Сообщение отправлено серверу.")
            received_data = client_socket.recv(1024)
            json_data = received_data.decode('utf-8')
            print (json_data)
            try:
                data = json.loads(json_data)
                print("Ответ от сервера:", data)
                return data
            except json.JSONDecodeError:
                print("Ошибка декодирования ответа сервера.")
                return None
    except Exception as e:
        print(f"Ошибка при подключении или обработке данных: {e}")
        return None
