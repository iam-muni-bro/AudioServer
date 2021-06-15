import socket
import threading

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
port=5000
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}:{port}")

server=socket.socket()
server.bind(('0.0.0.0',port))
server.listen(5)
clients=[]
def start():
    while(True):
        print("Server started ...")
        _connection,_ipAddress=server.accept()
        clients.append(_connection)
        print("Connection Accepted")
        t = threading.Thread(target=send,args=(_connection,_ipAddress))
        t.start()
def send(fromConnection,ipAdress):
    try:
        while(True):
            data=fromConnection.recv(4096)
            for client in clients:
                if client != fromConnection:
                    client.send(data)
    except Exception as e:
        print("Client Disconnected",e)
        
start()
