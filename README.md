# APIs-REST-microsservi-os

[![Coverage Status](https://coveralls.io/repos/github/kennedimalheiros/APIs-REST-microsservicos/badge.svg?branch=main)](https://coveralls.io/github/kennedimalheiros/APIs-REST-microsservicos?branch=main)
[![Build Status](https://travis-ci.org/kennedimalheiros/APIs-REST-microsservicos.svg?branch=main)](https://travis-ci.org/kennedimalheiros/APIs-REST-microsservicos)

O sistema é composto de dois projetos.

#
O projeto SERVER está configurado para rodar na porta 8001 ex: 127.0.0.1:8001, o arquivo 
Makefile já esta configurado para isso.

- Acesse a pasta server

        
    cd server/

- Execute o projeto SERVER crie o super usuário para adicionar os produtos pelo admin.


    make migrate
    make superuser

- Popule o banco de dados do SERVER com o comando:
  
  
    make populate
    make runserver

     
#
O projeto CLIENT pode ser executado em qualquer porta.

- Acesse a pasta client
        
        
    cd client/

- Execute o Projeto CLIENT


    make migrate
    make runserver

#

A documentação do API está disponivel ao acesar o projeto:


        127.0.0.1:8000
        127.0.0.1:8001
        

Ao acessar a api CLIENT passando o código de barras, o mesmo irá verificar em sua base de dados, caso não encontre o 
produto internamente ele faz acesso a api SERVER e armazena essa informação no projeto CLIENT para as próximas consultas.


    127.0.0.1:8000/product/{barcode}/