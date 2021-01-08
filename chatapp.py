import threading
import socket
friend_name=input("Enter your friend's name: ")
friend_ip=input("Enter your friend's IP: ")

#getting host ip
def ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipv4=s.getsockname()[0]
    s.close()
    return ipv4

ip=ip_address()
port=9459
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((ip,port))
print(ip)

#recieving message
def recv():
    while True:
        x=s.recvfrom(1024)
        print(f"{name}-> " + x[0].decode())

        if x[0].decode()=="exit":
            exit()

#sending message
def send():
    while True:
        text = input()
        print("You-> "+text)
        s.sendto(text.encode(),(friend_ip,9459))

re = threading.Thread(target=recv)
se = threading.Thread(target=send)

re.start()
se.start()