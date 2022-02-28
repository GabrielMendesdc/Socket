#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
#CLIENTE
host = '127.0.0.1'
porta = 50000
caminho = (host, porta)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(caminho)
while True:
    text = input()
    s.sendall(str.encode(text))

    dados = s.recv(1024)
    if dados.decode() == 'exit':
        break

    print(f'mensagem recebida: {dados.decode()} - exit pra sair')

s.close()
