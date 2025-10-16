# Loops em Python
# Loop com while

# Instrução de Loop infinito
# while True:
#     print("Estou preso em um Loop")

# Exemplo 1
# Armazenar um valor máximo
valor_maximo = -999999

numero = int(input("Digite seu número valor"))

# Instrução while
while numero != -1:
    if numero > valor_maximo:
        valor_maximo = numero

    numero = int(input("Digite um valor -1 ou outro valor"))

print("O maior número foi: ", valor_maximo)

# Manter aninhamento de if com mensagem e variável a declarar

# Exemplo 2
num_par = 0
num_impar = 0
 
# Leia o primeiro número.
numero = int(input("Digite um número ou digite 0 para parar: "))
 
# 0 termina a execução.
while numero != 0:
    # Verifique se o número é ímpar.
    if numero % 2 == 1:
        # Aumente o contador de números pares.
        num_par += 1
        
    else:
        # Aumente o contador números de ímpares.
        num_impar += 1
    # Leia o número seguinte.
    numero = int(input("Digite um número ou digite 0 para parar: "))
 
# Imprimir resultados.
print("Números ímpares quantidade:", num_impar)
print("Números pares quantidade:", num_par)

#Exemplo 3 - counter para sair do loop
counter = 5
while counter != 0:
    print("Dentro do loop", counter)
    counter -= 1
    print("Fora do loop", counter)


# Atividade 1 - Desafio
secret_number = 777

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")



# Loop com FOR
# Exemplo com while antes do FOR
i = 0
while i < 100:
    i += 1

print("Quantas repetições", i)

# Exemplo com FOR

for i in range(100):
    pass

print("Quantas repetições", i)

# Exemplo 4
for i in range(2,10):
    pass

    print("Repetições", i) #Contagem final
print("Repetições", i) #Contagem com resultado

# Atividade 2 - Desafio Mississippi

# Instruções de Break e Continue
# break - exemplo

print("O Break instrução:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro do laço.", i)
print("Fora do loop.")

# continue - exemplo

print("Continuação instrução:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro do laço.", i)
print("Fora do loop.")

# Exemplo 5
num_maximo = -99999999
counter = 0

numero = int(input("Insira um número ou digite -1 para finalizar o programa: "))

while numero != -1:
    if numero == -1:
        continue
    counter += 1

    if numero > num_maximo:
        num_maximo = numero
    numero = int(input("Insira um número ou digite -1 para finalizar o programa: "))

if counter:
    print("O maior número é",  num_maximo)
else:
    print("Você não inseriu qualquer número.")

# Exemplo 6
letras = input("Digite a palavra \n")
usuario_letras = input("Digite o usuário \n")


for letras in usuario_letras:
    while letras != "teste":
        if letras == usuario_letras:
            continue
        print("Letras:", letras)
else: 
        print("Usuário", usuario_letras) 

# O Loop while e o ramo Else
# com while
j = 1
while j < 5:
    print(j)
    j += 1

else:
    print("Outro", j)

# com FOR
for j in range(5):
    print(j)
else:
    print("Outro", j)

# Atividade 3 - Desafio

# Exemplo 7

palavra = "Python"
for letras in palavra:
    print(letras, end="*")
 
# Exemplo 8
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

# Exemplo 9
texto = "Monty Presure Python"
for letras in texto:
    if letras == "P":
        break
    print(letras, end="")
 
# Operadores lógicos AND , OR , NOT

# contador > 0 and valor == 100
valor = 5

print(valor > 0)
print(not (valor <= 0))
 
print(valor != 0)
print(not (valor == 0))

# Exemplo 10
i = 1
j = not not i

print(i)
print(j)

#Exemplo 11 - Deslocamento 
valor = 17
valor_direta = valor >> 1
valor_esquerda = valor << 2
print(valor, valor_esquerda, valor_direta)
