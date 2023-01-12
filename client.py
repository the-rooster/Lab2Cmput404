import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



sock.connect(("www.google.com",80))

req = "GET / HTTP/1.1\r\nConnection: close\r\n\r\n"

sock.send(req.encode("utf-8"))

buffer = bytearray()
print("receivin")
part = sock.recv(1024)


while part:

    buffer.extend(part)
    part = sock.recv(4096)



sock.detach()

print(buffer.decode("latin-1"))
