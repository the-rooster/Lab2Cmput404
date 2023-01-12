import socket
import multiprocessing


def echo_server(connection : socket.socket,address):
    
    part = connection.recv(4096)
    buffer = bytearray()

    while part:
        buffer.extend(part)
        part = connection.recv(4096)
    
    print(buffer.decode("utf-8"))
    
    connection.send(buffer)

    return
def main():

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.bind(("127.0.0.1",8001))

    while True:

        s.listen()

        connection, address = s.accept()

        print(connection)

        p = multiprocessing.Process(target=echo_server,args=(connection,address))

        p.start()

    




if __name__ == "__main__":
    main()