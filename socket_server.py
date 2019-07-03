
import socket as skt


def chat_server():
    HOST = "127.0.0.1"
    PORT_NO = 8080

    server = skt.socket() 
    server.bind((HOST, PORT_NO))

    server.listen(2)
    conn, address = server.accept()
    print("Request from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from user: " + str(data))
        data = input(' ---> ')
        conn.send(data.encode()) 

    conn.close()


if __name__ == '__main__':
   chat_server()
