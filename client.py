import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_HOST, SERVER_PORT)) # s.bind() funciona apenas para subir um servidor escutando em tal porta
# Enviado dados ao servidor
s.sendall(str.encode('Testando conexão'))
# Recebendo dados do servidor
serverResponse = s.recv(1024)
response = serverResponse.decode('utf-8')
print(response)

s.close()