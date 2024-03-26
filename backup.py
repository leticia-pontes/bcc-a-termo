import random

palavras = [ "abrir", "bravo", "canto", "dados", "bolas",
             "fugir", "grito", "hotel", "irado", "jogar",
             "luzes", "maior", "nível", "preto", "arroz",
             "quero", "risco", "saldo", "terra", "pingo",
             "viver", "limão", "mamão", "bingo", "viver" ]

termo = random.choice(palavras)

letras = list(termo)

print(letras)

# Loop (tentativas = for); palavra digitada (input); comparar; mostrar acertos
vidas = 4

# while vidas != 0:

# Abriga quais letras tão na posição certa
acertos = []

palavra_digitada = input()
vetor_palavra = list(palavra_digitada)

for i in range(0, 5):
    if vetor_palavra[i] == letras[i]:
        acertos.append(i)

print(acertos)

