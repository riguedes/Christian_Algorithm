# Bibliotecas necessárias para estabelecer a conexão e fornecer a hora de acordo com o Algoritmo de Christian
from socket import *
from datetime import *
import threading

local_servidor = "localhost"
porta = 9099

# Estabelecendo a conexão TCP
socket_servidor = socket(AF_INET, SOCK_STREAM)
socket_servidor.bind((local_servidor, porta)) # Encontrando o servidor e a porta definidas anteriormente
socket_servidor.listen() # Escutando a porta de conexão

def handle_client(socket_conexao, addr):
    print(f"Conectado com cliente {addr}")
    hora = datetime.now() # cálculo da hora e da data
    hora_master = hora.strftime("%Y%m%d %H:%M:%S.%f") # codificação no formato string
    print(f"Envio de hora ao cliente {addr}: {hora_master}")
    socket_conexao.send(hora_master.encode())
    socket_conexao.close() # encerrando a conexão
    print(f"Conexão encerrada com cliente {addr}")

# Gerando um ciclo infinito em relação às requisições
print(f"Servidor iniciado e escutando em {local_servidor}:{porta}")
while True:
    socket_conexao, addr = socket_servidor.accept() # retorna a conexão e o endereço do cliente
    print(f"Conexão aceita de {addr}")
    client_thread = threading.Thread(target=handle_client, args=(socket_conexao, addr))
    client_thread.start()
    print(f"Thread iniciada para cliente {addr}")