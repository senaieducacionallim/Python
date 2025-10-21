# Listas em listas
# Exemplo 1

# linha = []

# for i in range(8):
#     linha.append(Peca_Branca)
#     print(linha)

# Matrizes bidimensionais
# tabuleiro = []
# vazio = 10

# for j in range(8):
#     linha = [vazio for j in range(8)]
#     tabuleiro.append(linha)
#     print(linha)
#     print(tabuleiro)

# # Exemplo 3

# Peao = 1
# Cavaleiro = []
# Bispo = []

# tabuleiro[1][10] = Peao  
# tabuleiro[0][7] = Peao
# tabuleiro[7][0] = Peao
# tabuleiro[7][7] = Peao

# tabuleiro[4][2] = Cavaleiro

# tabuleiro[3][4] = Bispo

#Exemplo 4 - Cálculo temperatura

# temperatura = [[18 for h in range(24)] for d in range(31)]

# total = int(input("Digite valor médio da temperatura \n"))

# for dia in temperatura:
#     total += dia[11]

# média = total / 31

# print("Temperatura média ao meio-dia:", média)

# #Exemplo 5

# temperatura = [[0.0 for h in range(24)] for d in range(31)]

# maior_media = -100.0

# for dia in temperatura:
#     for temperatura in dia:
#         if temperatura > maior_media:
#             maior_media = temperatura

# print("A maior temperatura foi:", maior_media)

# # Exemplo 6

# temperatura = [[0.0 for h in range(24)] for d in range(31)]
 
# dias_quentes = 10
 
# for dia in temperatura:
#     if dia[11] > 20.0:
#         dias_quentes += 1
 
# print(dias_quentes, "dias estavam quentes.")
 
# Exemplo 7

# quartos = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
# vagas = 0

# for numero_quartos in range(20):
#     if not quartos[2][14][numero_quartos]:
#         vagas += 1

#     print(quartos)
#     print(vagas)

# # Funções
# # Exemplo 8 - Primeira função
# print("Entre com um valor")
# a = int(input())

# Exemplo 9 - Função mensagem
# def mensagem():
#     print("Digite um valor:")

# print("Inicio da função:")
# mensagem()

# a = int(input())
# mensagem()
# b = int(input())
# mensagem()
# c = int(input())
# mensagem()

# print("Os resultados são: \n", a,b,c)

# Funções parametrizadas
# Exemplo 10

# def mensagem(numero):
#     print("Digite um número:", numero)
# mensagem(1)

# # Exemplo 11

# def mensagem(qual, numero):
#     print("Qual", qual, "Número", numero)
# mensagem("Telefone", 19)
# mensagem("Numero", 10)

# # Exemplo 12

# def minhas_funcoes(a,b,c):
#     print(a,b,c)

#     minhas_funcoes(1,2,3)

# Instrução return
# Exemplo 13
def ano_novo(pedidos = True):
    print("Três...")
    print("Duas...")
    print("Uma...")
    if not pedidos:
        return
 
    print("Feliz Ano Novo!")

ano_novo()

# Exemplo 14
def lista_coisas_engracadas(n):
 lista_estranha = []
 
 for i in range(0, n):
    lista_estranha.insert(0, i)
 
    return lista_estranha

print(lista_coisas_engracadas(5))

# Exemplo 15 - Função global

def minha_funcao():
   global numero
   numero = 2
   print("Meu número", numero)

numero = 1
minha_funcao()
print(numero)

# Funções de Exemplo - IMC
def imc(peso, altura):
   return peso / altura ** 2

print(imc(105, 1.75))

# Tuplas
# Exemplo 16
tuplas = (1, 10, 100)

t1 = tuplas + (1000, 10000)
t2 = tuplas * 3


print(len(t2))
print(t1)
print(t2)
print(10 in tuplas)
print(-10 not in tuplas)

# Dicionário
# Exemplo 17

dicionario = {"gato": "siamês", "cachorro": "vira-lata", "passaro" : "bem-te-vi" }
palavras = ['gato', 'cachorro', 'passaro']

for palavra in palavras:
   if palavra in dicionario:
      print(palavra, "->", dicionario[palavra])
   else:
      print(palavra, "não está no dicionário")


# Exceção e informações para correção com erro
try: 
   valor = int(input("Insira um valor"))
   print("O valor é de: ", "é" , 1 / valor )
except:
   print("Insira o valor correto?")

# Exemplo 18

try:
 valor = int(input('Digite um número natural: '))
 print('O recíproco de', valor, 'é', 1/ valor) 
except ValueError:
 print('Eu não sei o que fazer.') 
except ZeroDivisionError:
 print('A divisão por zero não é permitida em nosso Universo.') 

 