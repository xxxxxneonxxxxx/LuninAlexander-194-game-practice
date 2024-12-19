import socket
import json
from CRUDD import *

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('0.0.0.0', 12331))

server_socket.listen(5)
print("Ожидание подключений...")


def handle_client(client_socket, addr):
    print(f"Подключен клиент с адресом: {addr}")

    try:
        received_data = client_socket.recv(4096)
        json_data = received_data.decode('utf-8')
        print(f"Получено сообщение: {json_data}")
        try:
            client_message = json.loads(json_data)
        except json.JSONDecodeError:
            client_socket.sendall(json.dumps({'error': 'Invalid JSON format'}).encode('utf-8'))
            return

        zapros = client_message.get('message')
        if not zapros:
            client_socket.sendall(json.dumps({'error': 'Missing "message" field'}).encode('utf-8'))
            return

        if zapros == "add_user":
            nickname = client_message.get('nickname')
            password = client_message.get('password')
            if not nickname or not password:
                client_socket.sendall(json.dumps({'error': 'Missing "nickname" or "password"'}).encode('utf-8'))
                return
            if add_user(nickname, password):
                client_socket.sendall(json.dumps({'status': 'User added successfully'}).encode('utf-8'))
            else:
                client_socket.sendall(json.dumps({'status': 'Failed to add user'}).encode('utf-8'))
        elif zapros == "READ_PROV":
            nickname = client_message.get('nickname')
            password = client_message.get('password')
            if READ_PROV(nickname, password):
                client_socket.sendall(json.dumps({'message': 'ok'}).encode('utf-8'))
            else:
                client_socket.sendall(json.dumps({'message': 'no'}).encode('utf-8'))


        elif zapros == "SORT_TIME":
            tip = client_message.get('tip')
            if not tip:
                client_socket.sendall(json.dumps({'error': 'Missing "tip" field for SORT_TIME'}).encode('utf-8'))
                return
            client_socket.sendall(json.dumps({'message': 'yes', 'table': SORT_TIME(tip)}).encode('utf-8'))

        elif zapros == "add_time":
            user_name = client_message.get('user_name')
            time_baza = client_message.get('time_baza')
            time_type = client_message.get('type')
            if not user_name:
                client_socket.sendall(json.dumps({'error': 'Missing "user_name"'}).encode('utf-8'))
                return
            if not time_baza:
                client_socket.sendall(json.dumps({'error': 'Missing "time_baza"'}).encode('utf-8'))
                return
            if not time_type:
                client_socket.sendall(json.dumps({'error': 'Missing "type"'}).encode('utf-8'))
                return
            if add_time(user_name, time_baza, time_type):
                client_socket.sendall(json.dumps({'status': 'Time added successfully'}).encode('utf-8'))
            else:
                client_socket.sendall(json.dumps({'status': 'Failed to add time'}).encode('utf-8'))
        else:
            client_socket.sendall(json.dumps({'error': 'Unknown request'}).encode('utf-8'))

    except Exception as e:
        print(f"Ошибка обработки данных: {e}")
        client_socket.sendall(json.dumps({'error': str(e)}).encode('utf-8'))

    finally:
        client_socket.close()
        print(f"Соединение с клиентом {addr} закрыто.")

while True:
    client_socket, addr = server_socket.accept()
    handle_client(client_socket, addr)
