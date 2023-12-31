import socket

HOST = '127.0.0.1'
PORT = 8888
server = (HOST, PORT)

# Declarando tipo de cconexão TCP IPV4 com socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Comninando endereço e porta do servidor na variável s do socket
s.bind((HOST, PORT))

# Socket em escuta
s.listen()
print("\nAGUARDANDO CONEXÃO...")

# Aceitando conexão do cliente
clientConn, clientAddress = s.accept()
print(f"\nCONEXÃO DE {clientAddress}")

while True:
    data = clientConn.recv(1024)
    if not data:
        print("CONEXÃO ENCERRADA")
        clientConn.close()
        break
    else:
        dataContent = data.decode('utf-8')
        print('DADOS RECEBIDOS DO CLIENTE: ', dataContent)
        clientConn.sendall(str.encode('SERVER OK - STATUS 200'))
