import adivinhacao
import forca

def escolher_jogo():
    print('-----------------------------------')
    print('----Bem vindo ao jogo de Forca!----')
    print('-----------------------------------')

    print('(1) Forca (2) Adivinhação')

    jogo = int(input('Qual o jogo? '))

    if (jogo == 1):
        print('Jogando Forca')
        forca.jogar()
    elif (jogo == 2):
        print('Jogando Adivinhação')
        adivinhacao.jogar()

if(__name__ == '__main__'):
    escolher_jogo()