import socket
host='LocalHost'
port=5656
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("Servidor en espera de conexiones ")
#cliente envia peticiòn y servidor nos devuelve direcciòn y objeto activo
active, addr = server.accept()

while True:
    recibidio=active.recv(1024)
    print("Cliente: ", recibidio.decode(encoding="ascii", errors="ignore"))
    enviar=input("Server: ")
    active.send(enviar.encode(encoding="ascii", errors="ignore"))

active.close()

