#!/usr/bin/python3

import socket
# AF_INET = we are using IPv4 ## SOCK_STREAM = TCP Connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1024)
s.bind(("127.0.0.1", 8888))
print("listening....")
s.listen(1)
client, addr = s.accept()
print("[+] Connected")

while True:
    cmd = input("$ ")
    client.send(cmd.encode())
    if cmd == "exit":
        break
    output = client.recv((1024)).decode()
    print(output)

client.close()
s.close()
print("[-] Connection Closed")