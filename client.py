import socket
host = 'Localhost'
port = 5656

#ocurrencia de socket
objsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
objsocket.connect((host,port))
print('Iniciamos cliente')

while True:
    enviar = input('Ingrese el mensaje: ')
    objsocket.send(enviar.encode(encoding="ascii",errors="ignore"))
    recibido= objsocket.recv(1024) # 1024 caracteres
    print("Servidor ", recibido.decode(encoding="ascii",errors="ignore"))

objsocket.close()