import socket

# Declarando variáveis de conexão para conectar com o servidor
SERVER_HOST = '192.168.15.10' # Endereço do servidor
SERVER_PORT = 8888 # Porta de conexão
server = (SERVER_HOST, SERVER_PORT)

# Definindo socket de conexão TCP IPV4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando com o servidor
s.connect(server)

# Enviado dados ao servidor
packet = 'Testando conexão'
s.sendall(str.encode(packet))

# Recebendo dados do servidor
serverResponse = s.recv(1024)
response = serverResponse.decode('utf-8')
print(response)

# Encerrando socket de conexão com o servidor
s.close()
