import socket
import json

def output_us(output):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(('server.pbtusur.ru', 12345))
            print("Подключение к серверу установлено.")
            message_to_server = json.dumps(output)
            client_socket.sendall(message_to_server.encode('utf-8'))
            print("Сообщение отправлено серверу.")
            received_data = client_socket.recv(1024)
            json_data = received_data.decode('utf-8')
            print(f"Ответ от сервера (до декодирования): {json_data}")
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
