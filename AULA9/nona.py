# Listas em listas
# Exemplo 1

# linha = []

# for i in range(8):
#     linha.append(Peca_Branca)
#     print(linha)

# Matrizes bidimensionais
tabuleiro = []
vazio = 10

for j in range(8):
    linha = [vazio for j in range(8)]
    tabuleiro.append(linha)
    print(linha)
    print(tabuleiro)

# Exemplo 3
Peao = []
Cavaleiro = []
Bispo = []

tabuleiro[0][0] = Peao
tabuleiro[0][7] = Peao
tabuleiro[7][0] = Peao
tabuleiro[7][7] = Peao

tabuleiro[4][2] = Cavaleiro

tabuleiro[3][4] = Bispo