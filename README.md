# ⏱️ Algoritmo de Sincronização de Relógios de Christian
Este repositório contém uma implementação em Python do Algoritmo de Christian para sincronização de relógios em sistemas distribuídos. O algoritmo utiliza um servidor de tempo confiável para ajustar os relógios dos clientes com base no tempo estimado de transmissão da mensagem.

## 📌 Objetivos
1. Implementar o algoritmo de sincronização de Christian em Python;
2. Simular a comunicação entre um servidor de tempo e múltiplos clientes;
3. Demonstrar o ajuste de relógios baseado no tempo de resposta estimado.

## 📌 Tecnologias Utilizadas
- Python (Linguagem principal)
- Sockets (Para comunicação entre servidor e clientes)
- Time (Para manipulação e medição de tempo)
- Threading (Para simular clientes concorrentes)

## 📊 Funcionamento do Algoritmo de Christian
1. O cliente solicita o tempo atual ao servidor.
2. O servidor responde com sua marcação de tempo.
3. O cliente calcula o atraso da mensagem e ajusta seu relógio de acordo.

O ajuste do tempo no cliente é feito da seguinte forma:

```
T_cliente = T_servidor + (T_round_trip / 2)
```

Onde:
- `T_servidor` é o tempo enviado pelo servidor.
- `T_round_trip` é o tempo total de ida e volta da mensagem.
- `T_round_trip / 2` é a estimativa do tempo de atraso de transmissão.

## 🚀 Como Executar o Projeto
1. Inicie o servidor de tempo:
   ```sh
   python src/server.py
   ```
2. Em outra janela de terminal, execute um ou mais clientes:
   ```sh
   python src/client.py
   ```

## 📌 Exemplo de Saída
Servidor:
```
[Servidor] Tempo atual: 1640995200.123456
[Servidor] Resposta enviada ao cliente.
```

Cliente:
```
[Cliente] Tempo recebido do servidor: 1640995200.123456
[Cliente] Tempo ajustado: 1640995200.223456
```
