import socket

# Correcion de binario a texto
def binary_to_text(binary_msg):
    text = ''.join(chr(int(binary_msg[i:i+8], 2)) for i in range(0, len(binary_msg), 8))
    return text

def hamming_correct(binary_msg):
    # Simular corrección de errores utilizando el código Hamming
    # Este es un ejemplo simple que solo invierte el bit en la posición 3
    corrected_binary_msg = binary_msg[:3] + ('0' if binary_msg[3] == '1' else '1') + binary_msg[4:]
    return corrected_binary_msg

host = 'localhost'
port = 5656
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
print("Servidor en espera de conexiones ")

active, addr = server.accept()

while True:
    recibido = active.recv(1024)
    print("Mensaje en binario recibido por el servidor:", recibido.decode())  # Mostrar el mensaje binario recibido

    # Simular error
    if '1' in recibido.decode():
        print("Mensaje con error detectado")
        error_message = binary_to_text (recibido.decode())
        print("Mensaje con error: ", error_message)
        corrected_binary_msg = hamming_correct(recibido.decode())  # Aplicar la corrección de errores
        print("Mensaje en binario corregido por el servidor:", corrected_binary_msg)  # Mostrar el mensaje binario corregido
        corrected_message = binary_to_text (corrected_binary_msg)
        print("Mensaje corregido: ", corrected_message)
        active.send(corrected_binary_msg.encode())  # Envía el mensaje binario corregido al cliente
    else:
        print("Mensaje sin errores")
        print("Mensaje recibido:", recibido.decode())  # Mostrar el mensaje binario recibido sin errores
        active.send(recibido)  # Devuelve el mensaje original al cliente

active.close()
