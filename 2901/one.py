import socket
import datetime
import random

texts = ["text1", "text2", "text3"]

def text():
    return random.choice(texts)

def date():
    return str(datetime.datetime.now())

def help():
    return "quote, date, help, exit, shutdown-server"

commands = {"text": text, "date": date, "help": help}

server_socket = socket.socket()
server_socket.bind(("127.0.0.1", 65430))
server_socket.listen()

while True:
    print("Server starts at 127.0.0.1:65430 :D")
    connection, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    while True:
        command = connection.recv(1024).decode().strip()

        if command == "exit":
            print("Client disconnected")
            connection.close()
            break

        elif command == "shutdown-server":
            print("Server is shutting down")
            connection.close()
            server_socket.close()
            exit(0)

        elif command in commands:
            response = commands[command]()
            connection.send(response.encode())

        else:
            response = "Unknown command"
