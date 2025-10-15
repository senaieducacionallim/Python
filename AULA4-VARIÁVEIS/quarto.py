# Variáveis
# Exemplo 1
caixa = 1
print("caixa")
print(caixa)

#Exemplo 2
banco = 1
conta = 1000
nome_cliente = "Bruno"
print("banco, conta, nome_cliente")
print("nome_cliente")
print(banco,conta,nome_cliente)
print(nome_cliente)

#Exemplo
print("Digite seu nome \n")
nome_usuario = "Bruno"
print(nome_usuario)

# Exemplo com sinal de + adição
curso = "Python"
print("Nosso curso é de: " + curso)

# Exemplo com sinal de + adição novo
seu_nome = "Bruno"
print("Qual é seu nome? \n" + seu_nome, "\n E seu curso é de: \n" + curso)

# Exemplo com operações + - * /
valor = 1
print(valor)
valor = valor + 5
print(valor)

# Exemplo com valores
a = 10
b = 20
c = a + b / 10 + 20
print("A soma dos valores é: \n", +c)

# Atividade 1 - Cisco
print("Bem-Vindo a Appleland")
john = 3
mary = 5
adam = 6
total_apples = john + mary + adam
print("Total de Maças é de: \n", + total_apples)

# Exemplo de solução da Cisco
john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=',')

total_apples = john + mary + adam
print(total_apples)

# Operadores de atalho
teste = 1
teste = teste + 1
teste += 1
print(teste)

x = 10
x = x * 2
x *= 2
print(x)

# Cenário 2 - Cisco com arredondar valores
km = 12.25
milhas = 7.383

milhas_por_km = 11.8878945
km_por_milhas = 7.6057

print(milhas, "milhas é", round(milhas_por_km, 2), "quilômetros")
print(km, "quilômetros é", round(km_por_milhas, 2), "milhas")

# Pergunta 1
# Qual é a saída do código a seguir?
ex1 = 2
ex1 = 3
print(ex1)
 
# Pergunta 2
# Quais dos seguintes nomes de variáveis são ilegais no Python? (Selecione três respostas)
# 101
# m 101
# del

# Pergunta 3
# Qual é a saída do trecho a seguir?
# 11

# Pergunta 4
# Qual é a saída do trecho a seguir?
# 1.0

# Exemplo de comentário a ser ajustado
#esse programa calcula o número de segundos em um dado número de horas
# esse programa foi escrito a dois dias atrás
# funções
a = 2 # número de horas
seconds = 3600 # número de segundos em uma hora

# emitir mensagem
print("Horas: ", a) #imprimindo o número de horas
# print("Seconds in Hours: ", a * seconds) # imprimindo o número de segundos em uma dada hora

#aqui também devería escrever "Adeus", mas o programador não teve tempo de escrever código
#esse é o final do programa que computa o número de segundos em 3 horas

# Mais um exemplo
# Este programa imprime
# uma introdução à tela.
print("Olá Mundo!")  # Chamando a função print()
print("Em Python.")
 
# Função Input
print("Meu nome é: \n")
nome = input()
print("Seu nome é" , nome)
print("E seu curso, qual é? ")
curso = input()
print("Meu curso é: ", curso)
print("Parabéns por estar estudando")

# Função Input com Idade
print("Informe sua idade:")
idade = input()
print("Sua idade é: ", idade)


a = 2025
print("Informe seu ano de nascimento")
# declaramos o b como int pois é valor inteiro
b = int(input()) 
c = a - b
print("Sua idade é", c)