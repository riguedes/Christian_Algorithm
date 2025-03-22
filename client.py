# Bibliotecas necessárias para o lado cliente do Algoritmo de Christian
from socket import *
import time # Biblioteca para contagem de tempo, calculando o tempo de execução
import datetime

# Função para converter para o tipo datetime
def conversao_hora_master(master):
    formato = '%Y%m%d %H:%M:%S.%f'
    hora_master = datetime.datetime.strptime(master, formato) # Ocorre a conversão da string
    return hora_master

IPServidor = "localhost" # Criação do próprio servidor
porta = 9099
socket_cliente = socket(AF_INET, SOCK_STREAM) # Inicialização do socket no lado cliente

# Início de contagem do tempo
inicio = time.time() # Armazenamento de um tempo aproximado
print(f"Conectando ao servidor {IPServidor}:{porta}")
socket_cliente.connect((IPServidor, porta)) # Resposta da requisição
print(f"Conexão estabelecida com o servidor")

# Recebendo a hora convertida
hora_master = socket_cliente.recv(4096).decode()
print(f"Hora recebida do servidor: {hora_master}")

final = time.time() # Conexão com o lado servidor para compreender a requisição
tempo = final - inicio # Descoberta do tempo total

hora = conversao_hora_master(hora_master)

print(f"O tempo total de ida e volta foi de: {tempo} segundos")
metade_tempo = tempo / 2 # Tempo aproximado da requisição do servidor
print(f"O tempo total de ida: {metade_tempo} segundos")
print(f"Hora do servidor: {hora_master}")
hora_exata = hora + datetime.timedelta(seconds=metade_tempo)
print(f"A hora exata é: {hora_exata.strftime('%H:%M:%S.%f')}")

socket_cliente.close()
print(f"Conexão com o servidor encerrada")