import socket
import threading

port=5000
host="0.0.0.0"
server=socket.socket()
server.bind((host,port))
server.listen(5)
client=[]
def start():
    while(True):
        print("Server started ...")
        conn,addr =server.accept()
        client.append(conn)
        print(f"Connection Accepted")
        t = threading.Thread(target=send,args=(conn,))
        t.start()
def send(fromConnection):
    try:
        while(True):
            data=fromConnection.rec(4096)
            for cl in client:
                if cl != fromConnection:
                    cl.send(data)
    except:
        print("Client Disconnected")

start()