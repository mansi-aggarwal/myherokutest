
import socket as skt


def chat_client():
    HOST = skt.gethostname()
    PORT_NO = 8080 

    client = skt.socket()
    client.connect((HOST, PORT_NO))

    msg = input(" ---> ")

    while msg.lower().strip() != 'bye':
        client.send(msg.encode()) 
        stream = client.recv(1024).decode() 

        print('server: ' + stream)

        msg = input(" ---> ") 

    client.close()


if __name__ == '__main__':
    chat_client()
