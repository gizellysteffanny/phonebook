# Gizelly Stefanny / Lidiane Marques / João Rafael

agenda = []         #Criando uma lista.

#Definindo as Funções:

def p_nome():       #Função para pedir o nome.
     return(input("Nome: "))


def p_telefone():   #Função para pedir o telefone.
     return(input("Telefone: "))


def p_celular():    #Função para pedir o celular.
     return(input("celular: "))


def p_email():      #Função para pedir o email.
     return(input("Email: "))


def listar_dados(nome, telefone, celular, email):      #Função que mostra todos os dados do contato.
     print("Nome: %s\nTelefone: %s\nCelular: %s\nEmail: %s" % (nome, telefone, celular, email))


def pesquisa(nome):           #Função para pesquisar contatos.
     name = nome.lower()     #Convertendo todas as letras em minúsculas.
     for d, e in enumerate(agenda):     #Executando o loop.
         if e[0].lower() == name:       #Determinando uma condição.
               return d                 #Executa caso a condição for verdadeira.
     return None                        #Executa caso a condição for falsa.
"""
* Foi atribuído o metodo lower para que não haja problemas
quando usuário digitar maiusculo e programa não reconhecer.
* Está usando a função enumerate para acessar a posição do elemento
e o próprio elemento.
* Função return para indicar o valor a retornar.
* Função return None,caso o dado não seja encontrado, não vai retornar nada.
"""


def novo():                   #Função para adicionar novo Contato.
     global agenda            #Definindo variável como Global.
     nome = p_nome()          #Entrada de dados.
     telefone = p_telefone()  #Entrada de dados.
     celular = p_celular()    #Entrada de dados.
     email = p_email()        #Entrada de dados.
     agenda.append([nome, telefone, celular, email]) #Adicionando os dados na agenda
"""
* Está sendo utilizada a variável global pois será possível o acesso
da mesma tanto dentro como fora da função, ou seja, pode ser acessada
por todas as funções do programa.
* Está sendo utilizado o método append para ser possível adicionar
novos dados durante a execução do programa na nossa agenda.
"""

def apagar():            #Função para apagar um contato.
     global agenda       #Definindo variável como Global.
     nome = p_nome()     #Entrada de dados.
     p = pesquisa(nome)  #Cria uma variável e chama a função pesquisa.
     if p != None:       #Determinando uma condição.
         del agenda[p]   #Executa caso a condição for verdadeira.
     else:
         print("Nome não encontrado.")  #Executa caso a condição for falsa.


def editar():                      #Função para editar um contato.
     p = pesquisa(p_nome())        #Entrada de dados.
     if p != None:                 #Determinando uma condição, caso seja verdadeira:
         nome = agenda[p][0]       #Procurando os dados na agenda.
         telefone = agenda[p][1]   #Procurando os dados na agenda.
         celular = agenda [p][2]   #Procurando os dados na agenda.
         email = agenda [p][3]     #Procurando os dados na agenda.
         print("Encontrado:")      #Exibi informação na tela.
         listar_dados(nome, telefone, celular, email) #Mostra os dados.
         nome = p_nome()           #Entrada dos novos dados editados.
         telefone = p_telefone()   #Entrada dos novos dados editados.
         celular = p_celular()     #Entrada dos novos dados editados.
         email = p_email()         #Entrada dos novos dados editados.
         agenda[p] = [nome, telefone, celular, email] #Armazenando os novos dados.
     else:
         print("Nome não encontrado.") #Executa caso a condição seja falsa.



def listar():                      #Função para mostrar lista de contatos.
     print("\nAgenda\n\n------")
     for e in agenda:
         listar_dados(e[0], e[1], e[2], e[3])
     print("------\n")

def pesquisar():                   #Função para Pesquisar os contatos.
     p = pesquisa(p_nome())        #Entrada de dados.
     if p != None:                 #Determinando uma condição, caso seja verdadeira:
         nome = agenda[p][0]       #Procurando os dados na agenda.
         telefone = agenda[p][1]   #Procurando os dados na agenda.
         celular = agenda [p][2]   #Procurando os dados na agenda.
         email = agenda[p][3]      #Procurando os dados na agenda.
         print("Encontrado:")      #Exibi informação na tela.
         listar_dados(nome, telefone, celular, email)  #Mostra os dados.
     else:
          print("Nome não encontrado.")      #Executa caso a condição seja falsa.

def validar(pergunta, inicio, fim):          #Função para validar numeros inteiros.
     while True:                             #Criando um loop infinito.
         try:                                #Criando um acordo/condição.
               valor = int(input(pergunta))  #Entrada de dados.
               if inicio <= valor <= fim:    #Deterimando uma condição.
                   return(valor)             #Executa caso for verdadeira.
               return                        
         except ValueError:                  #Executa caso for falsa.
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))
"""
Estamos usando a instrução Try-except, para tratar de um erro anormal,
inesperado que possa ocorrer durante a execução do programa.
Caso o usuário digite um dado diferente do tipo inteiro...
Vai gerar um erro de valor (ValueError) e irá fazer com que nosso
programa pare de funcionar e mostre uma mensagem de erro na tela.
Com isso, utilizamos essa instrução para criar nossa própria mensagem
de erro, e assim podemos também evitar a parada do nosso programa.
"""

def menu():                   #Função que exibe o menu de opções.
     print("""
   1 - Adicionar novo contato
   2 - Editar um contato
   3 - Pesquisar contato
   4 - Lista de contatos
   5 - Apagar um contato
   6 - Sair
""")
   
     return validar("Escolha uma opção: ",1,6) #Retorna o valor da opção desejada.


while True:                             #Criando um loop infinito.
     opção = menu()
     if opção == 6:                     
         break
     elif opção == 1:
         novo()
     elif opção == 2:
         editar()
     elif opção == 3:
         pesquisar()
     elif opção == 4:
         listar()
     elif opção == 5:
         apagar()
