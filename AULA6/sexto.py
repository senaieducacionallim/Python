# Tomada de decisões
# Sim isso é verdade 
# Não isso não é verdade

# igualdade ==
# var = 0 # Atribuindo 0 a var
# print(var == 0)

# var = 1 # Atribuindo 1 a var
# print(var == 0)

# texto = input("Mensagem \n")
# print(texto == "Olá \n")
# print(texto)

# # diferenças !=
# var = 0  # Atribuindo 0 a var
# print(var != 0)
 
# var = 1  # Atribuindo 1 a var
# print(var != 0)

# # Maior que > e Maior igual que >=
# var = 1
# print(var > 0)

# var = 2
# print(var >= 5)

# # Menor que < e Menor igual que <=
# var = 10
# print(var < 5)

# var = 5
# print(var <= 10)

#Exemplo
# valor = int(input("Digite o valor \n"))
# print(valor < 100)

# # Condições e execução condicional uso do IF
# tempo = input("Como está o tempo \n")
# if tempo:
#     tempo_bom()
# tempo_ruim()
# print(tempo)

# ovelhas = int(input("Digite a quantidade"))
# if ovelhas >= 120:
#     quantidade()
# print(ovelhas)

# Condições e execução condicional uso do IF e ELSE
# carros = int(input("Digite quantos carros \n"))
# if carros > 10:
#     True
# else: False
# print(carros)

# Exemplo 2
# numero1 = int(input("Digite o primeiro numero: \n"))
# numero2 = int(input("Digite o segundo numero: \n"))

# if numero1 > numero2:
#     total = numero1
# else: 
#     total = numero2
# print("O valor é:", total)

# Exemplo 3
numero3 = int(input("Digite o valor \n"))
numero4 = int(input("Digite o valor \n"))
if numero3 == numero4:
    total2 = numero3
else: 
    total2 = numero4
    print("O valor é:", total2)

 # Exemplo 4
numero5 = int(input("Digite um valor \n"))
if numero5 == 1:
    exemplo4 = print(numero5)
elif numero5 != 2:
    exemplo4 = print(numero5)
elif numero5 > 3:
    exemplo4 = True
else: numero5 = False
print("O valor é:", numero5)

# Exemplo 5
valor1 = int(input("Digite o valor \n"))
valor2 = int(input("Digite o valor \n"))

if valor1 > valor2: total = valor1
else: total = valor2

print("O resultado", total)

# Exemplo 6
valor1 = int(input("Digite o 1 valor"))
valor2 = int(input("Digite o 2 valor"))
valor3 = int(input("Digite o 3 valor"))

if valor1 == valor2: 
    total = valor1
    print(total)
elif valor2 > valor3:
    total = valor2
    print(total)
elif valor3 < valor1:
    total = valor3
    print(total)
else: 
    total = valor1
    print(total)

# Instruções de Loop

valor1 = int(input("Digite o 1 valor"))
valor2 = int(input("Digite o 2 valor"))
valor3 = int(input("Digite o 3 valor"))

valor_alto = max(valor1, valor2, valor3)
print("O valor mais alto é \n", valor_alto)

valor1 = int(input("Digite o 1 valor"))
valor2 = int(input("Digite o 2 valor"))
valor3 = int(input("Digite o 3 valor"))

valor_baixo = min(valor1, valor2, valor3)
print("O valor mais baixo é \n", valor_baixo)

# Exemplo 7
valor_entrada = float(input("Digite o valor"))

if valor_entrada > 5000:
    taxa = valor_entrada * 0.18 - 550.62

    taxa = round(taxa,0)
    print("O valor de cálculo:", taxa)
else: 
    print("Não possui taxa")


# Exemplo 8

year = int(input("Digite um ano: \n"))

if year < 1800:
    print("Quando tudo começou")
else: 
    print("Ainda estamos bem")

# Exemplo / Atividade 1

year = int(input("Digite seu ano de nasc \n"))

if year >= 1980:
    print("Nostalgia")

elif year > 1990 and year < 2000:
    print("Ano Dourados")

elif year > 2000 and year < 2010:
    print("Ano da Tecnologia")

else:
    print("Nos dias de hoje")


# Lista de revisão
# 1. Uma unica declaração IF
x = int(input("Digite um número"))

if x == 10:
    print("X = 10")

# 2. Uma série de declarações

x = int(input("Digite um número"))

if x > 5:
    print("X é maior que 5")

if x < 10:
    print("X é menor que 10")

if x == 10:
    print("X = 10")

# Uma declaração IF-ELSE

x = int(input("Digite um número"))

if x < 10:
    print("X é menor que 10")

else: 
    print("X é maior que 10")

# Uma declaração de IF-ELSE-ELIF

