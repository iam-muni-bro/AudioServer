import socket
import threading
import pyaudio
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")

client= socket.socket()
host=ip_address
port=5000

client.connect((ip_address,5000)) #here the ip is where you want to connect
p = pyaudio.PyAudio()
Format=pyaudio.paInt16
Chunks=4096
Channels=2
Rate=44100
#Stream input
input_stream=p.open(format=Format,channels=Channels,rate=Rate,input=True,frames_per_buffer=Chunks)
#Stream output
output_stream=p.open(format=Format,channels=Channels,rate=Rate,output=True,frames_per_buffer=Chunks)

def send():
    while True:
        try:
            data=input_stream.read(Chunks)
            client.send(data)
            print("sending")
        except:
            break
def receive():
    while True:
        try:
            data=client.recv(Chunks)
            output_stream.write(data)
            print("Receiving")
        except:
            break

t1=threading.Thread(target=send)
t2=threading.Thread(target=receive)

t1.start()
t2.start()

t1.join()
t2.join()

input_stream.stop_stream()
input_stream.close()
output_stream.stop_stream()
output_stream.close()
p.terminate()