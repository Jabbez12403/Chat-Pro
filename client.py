import time, socket, sys

print("\nWelcome to Chat Room\n")
print("Initializing...\n")
time.sleep(1)

s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = input(str("Enter server address: "))
name = input(str("\nEnter your name: "))
port = 1234
print("\nTrying to connect to", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")

message = ""
flag = False

while True:
    if flag:
        message = input(str("Me: "))
        if message == "[e]":
            s.send(message.encode())
            print("\nYou left the chat room!")
            break
        s.send(message.encode())
        message = s.recv(1024)
        flag = False
    else:
        message = s.recv(1024)
        message = message.decode()
        if message == "[e]":
            print(s_name, "has left the room.")
            print("\nConnection closed!")
            break
        print(s_name, ":", message)
        s.send(message.encode())
        flag = True