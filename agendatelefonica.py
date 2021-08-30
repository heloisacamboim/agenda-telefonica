# -*- coding: utf-8 -*-
"""AgendaTelefonica.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DrzGCPubX6MJTM1geqiFdPrCcPp4mD4C

##Agenda telefônica em Python

Aluna: Heloísa Martins Camboim de Sá<br>
Matrícula: 2172190236
"""

# Criação de dicionario vazio
agenda = {}

# Função que insere quantidade desejada de novos contatos
def inserirContato(nome,email,telefone,usuarioInstagram,usuarioTwitter):
  agenda[nome]=[telefone,email,usuarioInstagram,usuarioTwitter]
  

cont = int(input('Quantos contatos deseja inserir? '))
while cont > 0:
  nome = input('Nome: ')
  telefone = input('Telefone: ')
  email = input('E-mail: ')
  usuarioInstagram = input('Nome de usuario Intagram: @')
  usuarioTwitter = input('Nome de usuario Twitter: @')
  cont -= 1
  inserirContato(nome,email,telefone,usuarioInstagram,usuarioTwitter)

# Função que consulta dados de contatos existentes a partir do nome
def consultarContato():
  if nome in agenda:
    print(agenda[nome])
  else:
    print('Contato inexistente')

nome = input('Informe o nome que deseja consultar: ')
consultarContato()

# Função que exclui todos os dados de usuário a partir do nome
def removerContato():
  nome = input('Informe o nome do contato que deseja remover: ')
  if nome in agenda:
    del agenda[nome]
    print("Contato", nome, "removido com sucesso.")
  
removerContato()

# Função que altera dados de contato

def alterarContato(nome,telefone,email,usuarioInstagram,usuarioTwitter):
  if nome in agenda.keys():
    agenda[nome][0] = telefone
    agenda[nome][1] = email
    agenda[nome][2] = usuarioInstagram
    agenda[nome][3] = usuarioTwitter
    print('Dados alterados com sucesso {} {} {} {} {}'.format(nome,agenda[nome][0],agenda[nome][1],agenda[nome][2],agenda[nome][3]))
  else:
    print("Nome não encontrado!")

# Solicita o nome de contato e os dados que serao alterados
nome = input("Informe o nome que deseja alterar os dados: ")
telefone = input("Informe o novo telefone: ")
email = input("Informe o novo E-mail: ")
usuarioInstagram = input("Informe o novo nome de usário Instagram: ")
usuarioTwitter = input("Informe o novo nome de usário Twitter: ")

alterarContato(nome,telefone,email,usuarioInstagram,usuarioTwitter)

# Função que gera relatório contendo os dados dos contatos cadastrados

def listarContatos():
  print("Numero \t Nome \t Telefone \t E-mail \t\t\t Instagram \t Twitter")

  cont=1
  for i in agenda.keys():
    print("{}\t {}\t {}\t {}\t\t @{}\t @{}".format(cont,i,agenda[i][0],agenda[i][1],agenda[i][2],agenda[i][3]))
    cont += 1

listarContatos()

# Função que apresenta os dados dos contatos separados por virgula
def salvarDados():
  for i in agenda.keys():
    print('{}, {}, {}, {}, {}'.format(i,agenda[i][0],agenda[i][1],agenda[i][2],agenda[i][3]))

salvarDados()

# Função que apresenta o menu

def print_menu():
  print("Agenda Telefonica\n"
  "\n"
  "Menu\n"
  "1 - Inserir contato\n"
  "2 - Consultar contato\n"
  "3 - Remover contato\n"
  "4 - Alterar contato\n"
  "5 - Listar contatos\n"
  "6 - Sair")

# Solicita a opcao que sera executada
opcao = int(input('Informe a opcao desejada: '))

# Condicional que chama a funcao a ser executada
if opcao == 1:
  inserirContato()
elif opcao == 2:
  consultarContato()
elif opcao == 3:
  removerContato(agenda)
elif opcao == 4:
  alterarContato()
elif opcao == 5:
  listarContatos()
elif opcao == 6:
  print('FIM')
else:
  print('Opcao invalida!')