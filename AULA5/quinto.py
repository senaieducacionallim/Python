# Conversão de tipos com input
# Primeiro exemplo
valor1 = float(input("Digite um valor \n"))
valor_total = valor1 + 5
print("Valor Total é \n", + valor_total)

#Segundo exemplo com FLOAT
valor1 = float(input("Digite um valor \n"))
valor2 = float(input("Digite um outro valor \n"))
valor_total = valor1 + valor2
print("Valor Total é \n", + round(valor_total,2))

# Terceiro exemplo com input INT
valor3 = int(input("Digite sua idade \n"))
print("Sua idade é: \n", +valor3)

# Qaurto exemplo com input STRING não necessário o sinal de + adição
nome = input("Digite seu nome \n")
print("Seu nome é: ", nome)

# Operadores de string + *
pnome = input("Digite seu primeiro nome \n")
unome = input("Digite seu último nome \n")
print("Seu primeiro nome é:" + pnome + " " "Seu último nome:" + unome + " ")

# Conversões str para número
lado1 = float(input("Digite o primeiro lado \n"))
lado2 = float(input("Digite o segundo lado \n"))
print("A soma dos lados são: " + str(lado1 + lado2))

#Exemplo novo pode ser utilizado o + adição ou vírgula antes de chamar a variável
lado3 = input("Digite o terceiro lado \n")
print("O valor do lado é" + str(lado3))

