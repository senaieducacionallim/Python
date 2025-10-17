# Listas Índices (Index)

# Exemplo 1
numeros = [10, 5, 7, 2, 1]
print("Os valores da lista são: \n", numeros)

numeros[0] = 111
print("Lista com valor fixo: \n", numeros)

numeros[1] = numeros[4]
print("Lista com dois indices: \n", numeros)

# Exemplos de impressão de valores no indice
print(numeros[0]) # Imprimir valor
print(numeros[4])
print(numeros[3])

print("Tamanho da lista", len (numeros)) # Imprimir comprimento da lista

# ---------------------------------

# Exemplo 2 - Remover elementos da lista
# del numeros[1]
# print(len(numeros))
# print(numeros)

# del numeros[2]
# print(len(numeros))
# print(numeros)

# Exemplo 3
numeros[1] = numeros[3]
print("Conteúdo da lista anterior: \n", numeros)
print("Comprimento da lista", len (numeros))

del numeros[1]
del numeros[3]
print("Comprimento da nova lista", len (numeros))
print("Nova lista de conteúdo", numeros)

# Exemplo de lista com valores negativos
numeros_novos = [111, 112, 113, 114, 116, 117]
print(numeros_novos[-2])
print("Comprimento da lista", len (numeros_novos))

# Atividade 1 - Desafio do Chapéu
# Era uma vez um chapéu. O chapéu não continha coelhos, mas uma lista de cinco números: 1, 2, 3, 4 e 5.

# Sua tarefa:

# escreva uma linha de código que solicite que o usuário substitua o número do meio na lista por um número inteiro inserido pelo usuário (Etapa 1)
# escreva uma linha de código que remova o último elemento da lista (Etapa 2)
# escreva uma linha de código que imprima o comprimento da lista atual (Etapa 3).

# Funções e métodos
# resultado = function() # Sintaxe
# resultado = () # Sintaxe

# Inserindo elementos na lista com append e insert
numeros_teste = [1,2,3,4]
print(len(numeros_teste))
print(numeros_teste)

numeros_teste.append(4) # Utilizar append inserir ()
print(len(numeros_teste))
print(numeros_teste)

numeros_teste.insert(5,200) #Utilizar insert inserir ()
print(len(numeros_teste))
print(numeros_teste)

#Exemplo 4
minha_lista = []

for i in range(5):
    minha_lista.append (i + 1)

print("Minha lista é: \n", minha_lista)

# Exemplo 5
minha_nova_lista = [10, 50, 2, 3]
total = 0

for j in range(len(minha_nova_lista)):
    total += minha_nova_lista[j]

print("O total da lista é: \n", total)

# Atividade 2 - Desafio

#Resumo - Listas de exemplos
# 1.
minha_lista_resumo = [1, None, True, "Eu sou Bruno", 256, 0]
print("Minha lista de resumo é: \n", minha_lista_resumo)
print("Minha lista com comprimento", minha_lista_resumo[3])
print("Minha outra lista", minha_lista_resumo[-2])


minha_lista_resumo = '?'
print("Meu coringa: \n", minha_lista_resumo)

# minha_lista_resumo.insert(0, "primeiro")
# minha_lista_resumo.append("ultimo")
print(minha_lista_resumo)

# 2.
cores = ["branco", "azul", "preto", "vermelho"]
for colors in cores:
    print("Minhas cores são: \n", colors)

# Ordenando listas simples 
# Exemplo 7
lista = [8, 7, 6, 2, 1]
for k in range(len(lista) -1):
    if lista[k] > lista[k + 1]:
        lista[k], lista[k + 1] = lista[k + 1], lista[k]
print("Minha lista ordenada: \n", lista)

# Exemplo 8 - Ordenação por bolhas

lista_vazia = []
swapped = True
numeros = int(input("Quantos elementos você deseja embaralhar? "))

for l in range(numeros):
 valor = float(input("Entre com a lista de elementos:"))
 lista_vazia.append(valor)

while swapped:
    swapped = False
    for i in range(len(lista_vazia) - 1):
        if lista_vazia[i] > lista_vazia[i + 1]:
            swapped = True
            lista_vazia[i], lista_vazia[i + 1] = lista_vazia[i + 1], lista_vazia[i]

print("\ Números sorteados:")
print(lista_vazia)

# Exemplo 9
lista_sorteada = [8, 10, 12, 2, 3]
lista_sorteada.sort()
print("Minha lista de valores é: \n", lista_sorteada)

# Exemplo 10
lista_alf = ["S", "T", "O", "L", "B"]
lista_alf.sort()
print("Minha lista com letras \n", lista_alf)

# Operações em listas - Fatiando
# Exemplo 11

lista_1 = [1]
lista_2 = lista_1[:]
lista_1[0] = 2
print("Imprimir lista", lista_2)

nova_lista = [10, 8, 5, 3]
total_lista = nova_lista[1:3]
print("Total de listas", total_lista)

# Nova lista com valores negativos
nova_lista = [10, 8, 5, 3]
total_lista = nova_lista[1:-2]
print("Total de listas", total_lista)

# Excluir elementos com lista
nova_lista = [10, 8, 5, 3]
del nova_lista[1:3]
print("Lista com valores removidos:\n",nova_lista)

# Operadores in e not in
# Exemplo 12

nova_lista = [0, 3 ,12 , 23, 33]
print(23 in nova_lista)
print(3 not in nova_lista)
print(12 in nova_lista)

# Exemplo 13 - Buscar o maior valor da lista
nova_lista = [1,2,14,20,30,50,70,40,22,62]
maior_valor = nova_lista[0]

for i in range(1, len(nova_lista)):
    if nova_lista[i] > maior_valor:
        maior_valor = nova_lista[i]

print("O maior valor é \n", maior_valor)

# Exemplo 14 - Com fatia no maior valor

nova_lista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
maior_valor = nova_lista[0]
 
for i in nova_lista[5:]:
    if i > maior_valor:
        maior_valor = i
 
print(maior_valor)

# Exemplo 15
nova_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
encontrar = 5
found = False
 
for i in range(len(nova_lista)):
    found = nova_lista[i] == encontrar
    if found:
        break
 
if found:
    print("Elemento encontrado no índice", i)
else:
    print("ausente")
 
# Exemplo 16
sorteados = [5, 11, 13, 23, 19, 30]
apostas = [3,12,15,20,21,33]
tentativa = [1,2]

for numeros in apostas:
    if numeros in sorteados:
        tentativa += 1

print("Valores \n", tentativa)
 
# Exemplo 17
lista = [1,2,3,4,5]
fatia_1 = lista[2: ]
fatia_2 = lista[ :2]
fatia_3 = lista[-2: ]

print(fatia_1)
print(fatia_2)
print(fatia_3)
