# Conexão TCP IPV4 com Python socket

Em redes de computadores, um socket IPv4 é uma combinação única de um endereço IP (Internet Protocol) e um número de porta. O IPv4 é a versão mais antiga do protocolo de Internet e utiliza endereços IP de 32 bits, normalmente expressos como quatro conjuntos de números separados por pontos, como "192.168.1.1". Já o número de porta identifica um processo específico em um dispositivo.

Assim, um socket IPv4 é identificado pela combinação do endereço IP e número de porta, permitindo a comunicação entre diferentes dispositivos em uma rede. Por exemplo, em um servidor web, o socket IPv4 seria algo como "192.168.1.1:80", onde "192.168.1.1" é o endereço IP do servidor e "80" é o número de porta associado ao serviço HTTP.

Os sockets são essenciais para a comunicação entre aplicativos na rede, permitindo que dados sejam enviados e recebidos de forma eficiente e organizada.

## Server.py

O arquivo `server.py` contém o código responsável por criar um servidor utilizando sockets TCP/IP para comunicação. Abaixo está a documentação detalhada do código:

### Variáveis de Conexão

- `HOST`: Representa o endereço IP do servidor. Atualmente configurado como '192.168.15.10', mas pode ser modificado para o endereço desejado.
  
- `PORT`: Representa a porta de conexão do servidor. Configurado como 8888, mas pode ser alterado conforme necessário.

- `server`: Tupla que combina o endereço IP e a porta para formar a identificação do servidor.

### Configuração do Socket

- `s`: Objeto de socket que utiliza o protocolo IPv4 (AF_INET) e o tipo de socket TCP (SOCK_STREAM). Em seguida, o endereço e a porta do servidor são associados a este socket.

### Inicialização do Servidor

- `s.listen()`: Coloca o socket em modo de escuta, permitindo que aceite conexões de clientes.

- `s.accept()`: Aguarda até que um cliente se conecte e aceita a conexão. Retorna uma nova socket (`clientConn`) e o endereço do cliente (`clientAddress`).

### Loop de Comunicação

- O servidor entra em um loop infinito, recebendo dados do cliente, decodificando-os e enviando uma resposta padrão ("SERVER OK - STATUS 200"). Se a conexão for encerrada pelo cliente, o loop é interrompido.

## Client.py

O arquivo `client.py` contém o código para criar um cliente que se conecta ao servidor. Abaixo está a documentação detalhada do código:

### Configuração do Cliente

- `SERVER_HOST` e `SERVER_PORT`: Representam o endereço IP e a porta do servidor ao qual o cliente se conectará.

- `connect_to_server()`: Função que tenta conectar-se ao servidor. Em caso de falha na conexão, aguarda por um tempo (2 segundos) e tenta novamente.

### Inicialização do Cliente

- `client_socket`: Objeto de socket criado chamando a função `connect_to_server()`.

### Enviando Dados ao Servidor

- `client_socket.sendall()`: Envia os dados ('Testando conexão') ao servidor após a conexão ser estabelecida.

### Recebendo Resposta do Servidor

- `client_socket.recv()`: Aguarda a resposta do servidor e a decodifica para exibição.

### Encerramento do Socket

- `client_socket.close()`: Encerra o socket de conexão com o servidor após a comunicação.

Essa documentação fornece uma visão geral do funcionamento do código, permitindo uma compreensão mais fácil e rápida das funcionalidades implementadas.
