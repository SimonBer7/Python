import socket
import datetime

def help():
    return "Write: quote, date, help, exit, shutdown-server"

def text():
    return "Random text"

def date():
    return str(datetime.datetime.now())


server_inet_address = ("127.0.0.1", 65430)
server_socket = socket.socket()
server_socket.bind(server_inet_address)
server_socket.listen()

while True:
    print("Server start on "+str(server_inet_address[0])+":"+str(server_inet_address[1]))
    connection, client_inet_address = server_socket.accept()
    print("Client connection accepted from "+str(client_inet_address[0])+":"+str(client_inet_address[1]))

    while True:
        # Receive the command from the client
        command = connection.recv(1024).decode().strip()

        # Handle the "exit" command
        if command == "exit":
            print("Client disconnected")
            connection.close()
            break

        # Handle the "shutdown-server" command
        elif command == "shutdown-server":
            print("Server is shutting down")
            connection.close()
            server_socket.close()
            exit(0)

        # Handle known commands
        elif command in text:
            response = text[command]()
            connection.send(response.encode())

        # Handle unknown commands
        else:
            response = "Unknown command"













