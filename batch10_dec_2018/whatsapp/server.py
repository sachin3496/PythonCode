import socket
host = socket.gethostbyname(socket.gethostname())
port = 12345
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))

server.listen()
print(f"Server is Running on {host}:{port}")
client,addr = server.accept()

print(f"\nClient request accept")
print(f"\nClient Address {addr[0]}:{addr[1]}\n")

while True : 

    smsg = input("server--> ")
    client.send(smsg.encode())
    cmsg = client.recv(1024).decode()
    print(f"\t\tclient-->{cmsg}")

    if smsg.lower().strip() == 'bye' or cmsg.lower().strip() == 'bye' : 
        break

client.close()
server.close()



