import time, socket, sys

print("\nWelcome to Chat Room\n")
print("Initializing...\n")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))

s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
conn.send(name.encode())

message = ""
flag = True

while True:
    if flag:
        message = input(str("Me: "))
        if message == "[e]":
            conn.send(message.encode())
            print("\nYou left the chat room!")
            break
        conn.send(message.encode())
        message = conn.recv(1024)
        flag = False
    else:
        message = conn.recv(1024)
        message = message.decode()
        if message == "[e]":
            print(s_name, "has left the room.")
            print("\nConnection closed!")
            break
        print(s_name, ":", message)
        conn.send(message.encode())
        flag = True