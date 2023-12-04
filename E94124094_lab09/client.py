import socket

c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s_address =('192.168.137.109',8000)
c.connect(s_address) #連線至遠端地址
print("connect to 192.168.137.109")

while True:
    outdata=input("The Fabonnaci(n) when n=") #輸入n值
    c.send(outdata.encode()) #用byte形式傳送資料
    if outdata == "exit":
        c.close()
        break
    indata=c.recv(1024) #接收答案
    print(f"the ans is {indata.decode()}")

