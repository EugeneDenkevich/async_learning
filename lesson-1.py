import socket


# Создаём сокет сервера. Назначаем семейство - IPv4, протокол передачи данных - TCP.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Конфигурируем переиспользование порта, чтобы не ждать при перезапуске программы.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Назначаем домен и порт сервера.
address = "localhost", 5000
server_socket.bind(address)

# Переводим сервер в режим прослушивания входящих подключений.
server_socket.listen()

# Цикл обработки входящих подключений.
while True:
    
    # Принимаем входящее подключение.
    print("До метода accept()")
    client_sock, addr = server_socket.accept()
    print("Connection from", addr)

    # Цикл обработки входящих сообщений подключения (клиента).
    while True:
        # Ожидаем получения сообщения и указываем размер буфера для сообщения 4кб.
        print("До метода recv()")
        request = client_sock.recv(4096)

        # Определяем, есть ли респонз и готовим ответ в виде bytes
        if not request:
            break
        else:
            response = "Hello, client!".encode()

            # Шлём ответ клиенту.
            client_sock.send(response)

    print("Снаружи внутреннего цикла.")
