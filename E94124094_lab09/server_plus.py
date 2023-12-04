import socket
import threading

HOST = '192.168.137.109'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def fibonacci(n):
    if n == 0 or n == 1:
        return str(n)
    ret = [0, 1]
    for i in range(n - 1):
        ret.append(ret[-1] + ret[-2])
    return str(ret[-1])

def handle_client(client_socket, address):
    print("Add connection from", address)
    
    while True:
        indata = client_socket.recv(1024).decode()
        print("Receive from", address, ":", indata)

        if indata == "exit":
            print("Connection closed for", address)
            client_socket.close()
            break

        outdata = fibonacci(int(indata))
        client_socket.send(outdata.encode())
        print("Send to", address, ":", outdata)

def main():
    while True:
        print("Waiting for connection...")
        client, addr = s.accept()
        client_thread = threading.Thread(target=handle_client, args=(client, addr))
        client_thread.start()

if __name__ == "__main__":
    main()