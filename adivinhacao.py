import random

def jogar():

    print('-----------------------------------')
    print('Bem vindo ao jogo de Adivinhação!')
    print('-----------------------------------')

    numero_secreto = random.randrange(1, 101)
    total_de_chances = 0
    pontos = 1000

    print('Qual dificuldade?')
    print('(1) Fácil (2) Médio (3) DIfícil')
    nivel = int(input('Selecione a dificulade: '))

    if (nivel == 1):
        total_de_chances = 20
    elif (nivel == 2):
        total_de_chances = 10
    else:
        total_de_chances = 5

    for chance in range(1, total_de_chances + 1):
        print('Você tem {} de {} chances'.format(chance, total_de_chances))
        chute = int(input('Digite um número: '))
        print('Você chutou: ', chute)

        if (chute < 1 or chute > 100):
            print('Você tem chutar um número entre 1 e 100!')
            continue

        if (numero_secreto == chute):
            print('Você acertou e fez {} pontos'.format(pontos))
            break
        else:
            if(chute > numero_secreto):
                print('Você errou! O seu chute foi maior do que o número secreto!')
            else:
                print('Você errou! O seu chute foi menor do que o número secreto!')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print('O número secreto é {}!'.format(numero_secreto))
    print('Fim do jogo!')

if(__name__ == '__main__'):
    jogar()
