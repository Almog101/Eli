# Import socket module
import socket




def Main():
    host = '127.0.0.1'
    port = 29811

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))

    while True:
        message = input("Enter message (enter 'quit' to exit): ")
        if message == 'quit':
            break

        s.send(message.encode())

        data = s.recv(1024)
        print('Received from the server :',str(data.decode()))

    s.close()

if __name__ == '__main__':
    Main()
