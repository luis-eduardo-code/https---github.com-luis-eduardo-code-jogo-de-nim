from calculos import Calculo
from rodadas import rodada



def campeonato():# funçao para o modo de jogo campeonato
    print("Você escolheu o campeonato!")
    rodadas = 3
    for i in range(rodadas):
        print('Rodada', i )
        rodada.partida()
    
    print("**** Final do campeonato! ****")
    print("Placar: Você 0 X 3 Computador")


def escolher_jogo(): # tratamento de erro para o modo de jogo
    print("Bem-vindo ao jogo de Nim!")
    try:
        modo_jogo = int(input("Escolha o modo de jogo \n "
                              "1. Partida \n "
                              "2. Campeonato \n "))
        while not (modo_jogo == 1 or modo_jogo == 2):
            print("Modo de jogo inválido! Tente novamente.")
            modo_jogo = int(input("Escolha o modo de jogo \n "
                                  "1. Partida \n "
                                  "2. Campeonato \n "))
        return modo_jogo
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return escolher_jogo()
        
def main():
     
     if escolher_jogo() == 1:
        print("Você escolheu jogar uma partida contra o computador!")
        rodada.partida()
     else:
       
         campeonato()

main()

   

    
   