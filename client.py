import socket
import time

SERVER_HOST = 'localhost'
SERVER_PORT = 8888

def connect_to_server():
    while True:
        try:
            print("\nAGUARDANDO RESPOSTA DO SERVIDOR...")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((SERVER_HOST, SERVER_PORT))
            return s
        except (socket.error, socket.timeout):
            print(f"\n\033[31mSem resposta, enviando nova requisição ao servidor em {SERVER_HOST}:{SERVER_PORT}\033[0;0;0m")
            time.sleep(2)

# Inicia a tentativa de conexão
client_socket = connect_to_server()

# Enviando dados ao servidor
packet = 'Testando conexão'
client_socket.sendall(str.encode(packet))

# Recebendo dados do servidor
serverResponse = client_socket.recv(1024)
response = serverResponse.decode('utf-8')
print(f'\n\033[1;34mRESPOSTA RECEBIDA:\n\033[0;0;0m{response}\n')

# Encerrando socket de conexão com o servidor
client_socket.close()
