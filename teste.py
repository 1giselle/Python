print("*************************")
print("Seja Bem-vindo ao teste de Adivinhação")

numero_secreto = 42

chute = input("Digite seu número: ")

chute = int(chute)


if(chute == numero_secreto):
    print("Parabéns, você acertou!")
else:
    print("Você errou")
print(Fim de jogo!)