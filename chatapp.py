import threading
import socket

#Information
name=input("Enter your friend's name: ")
friend_ip=input("Enter your friend's IP: ")

#Getting Host IP
def ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipv4=s.getsockname()[0]
    s.close()
    return ipv4

#Starting UDP Socket
ip=ip_address()
port=9459
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((ip,port))
print(ip)

#Recieving Message
def recv():
    while True:
        x=s.recvfrom(1024)
        print(f"{name}-> " + x[0].decode())

        if x[0].decode()=="exit":
            exit()

#Sending Message
def send():
    while True:
        text = input()
        print("You-> "+text)
        s.sendto(text.encode(),(friend_ip,9459))

#Starting Thread
re = threading.Thread(target=recv)
se = threading.Thread(target=send)

re.start()
se.start()