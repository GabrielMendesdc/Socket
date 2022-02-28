#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
#SERVIDOR
host = '127.0.0.1'
porta = 50000
caminho = (host, porta)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(caminho)
s.listen()

con, caminho_cliente = s.accept()

print(caminho_cliente)

while True:
    dados = con.recv(1024)
    con.sendall(dados)
    if not dados:
        break
    print('Mensagem recebida:  ', dados.decode())

s.close()
