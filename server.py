import socket
import threading
import _thread

IP = "127.0.0.1"
PORT = 29811

class Client(threading.Thread):
    def __init__(self, connection):
        self.connection = connection

    def run(self):
        while True:
            data = self.connection.recv(1024).decode()
            if not data:
                print('Bye')
                break
            print("Message Received: ", data)
            self.connection.send("got message".encode())
        self.connection.close()

class Server():
    def __init__(self, ip, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((ip, port))
        print("socket binded to port", PORT)

    def start(self):
        self.socket.listen(5)
        print("socket is listening")

        while True:
            connection, address = self.socket.accept()
            print('Connection from :', address[0], ':', address[1])

            _thread.start_new_thread(Client, (connection))

        self.socket.close()

    def stop(self):
        self.socket.close()

if __name__ == '__main__':
    server = Server(IP, PORT)
    try:
        server.start()
    except Exception as e:
        print(e)
        server.stop()
