import socket
import multiprocessing


def proxy_to_google(connection : socket.socket,address):
    
    part = connection.recv(4096)
    cl_buffer = bytearray()

    google_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    google_socket.connect(("www.google.com",80))

    #receive client input
    while part:
        print("READING CLIENT REQ")
        cl_buffer.extend(part)
        part = connection.recv(4096)

    print("PROXYING TO www.google.com: ",cl_buffer)
    #proxy request to google
    google_socket.send(cl_buffer)
    
    #get response from google
    g_buffer = bytearray()
    part = google_socket.recv(4096)
    print('read first bit')

    while part:
        g_buffer.extend(part)
        part = google_socket.recv(4096)

    
    print(g_buffer.decode("latin-1"))
    
    connection.send(g_buffer)
    connection.detach()
    return
def main():

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.bind(("127.0.0.1",8001))

    while True:

        s.listen()

        connection, address = s.accept()

        print(connection)

        p = multiprocessing.Process(target=proxy_to_google,args=(connection,address))

        p.start()

    




if __name__ == "__main__":
    main()