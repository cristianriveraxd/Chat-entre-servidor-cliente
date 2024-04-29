import socket

def text_to_binary(text):
    binary_msg = ''.join(format(ord(char), '08b') for char in text)
    return binary_msg

host = 'localhost'
port = 5656
objsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
objsocket.connect((host, port))
print('Iniciamos cliente')

while True:
    enviar = input('Ingrese el mensaje: ')
    binary_msg = text_to_binary(enviar)  # Convertir a binario
    print("Mensaje en binario enviado por el cliente:", binary_msg)  # Mostrar mensaje en binario

    simular_falla = input("¿Simular error en este mensaje? (Sí/No): ")
    if simular_falla.lower() == 'si':
        # Simular error cambiando un bit en el mensaje binario
        enviar_con_error = binary_msg[:3] + '1' + binary_msg[4:]  # Cambiar el cuarto bit
        objsocket.send(enviar_con_error.encode())  # Envía el mensaje en binario con error
        recibido = objsocket.recv(1024)
        print("Servidor (mensaje con error corregido): ", recibido.decode())  # Mostrar el mensaje incorrecto recibido del servidor
    else:
        objsocket.send(binary_msg.encode())  # Envía el mensaje en binario sin error
        recibido = objsocket.recv(1024)
        print("Servidor (mensaje corregido): ", recibido.decode())  # Mostrar el mensaje corregido recibido del servidor

objsocket.close()
