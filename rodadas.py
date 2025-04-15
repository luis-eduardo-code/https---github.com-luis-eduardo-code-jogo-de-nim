from calculos import Calculo
"""classe que define a rodada do jogo"""
class rodada:

    def valores():
        while True:
            try:
                print("Por favor, insira as configurações do jogo:")
                n= int(input("Quantas peças? "))
                m= int(input("Limite de peças por jogada? "))
                while n <= 0 or m <= 0:
                     print("Oops! O número de peças deve ser maior que 0 e o limite de peças por jogada deve ser maior que 0. Tente de novo.")
                     n= int(input("Quantas peças? "))
                     m= int(input("Limite de peças por jogada? "))
                return n,m
            except ValueError:
                 print('Entrada inválida. Por favor, digite um número inteiro.')
                 return rodada.valores()
# definindo a função partida que recebe o número de peças e o número máximo de peças que podem ser retiradas


    def partida():
        """função que define a partida"""
    
        n,m = rodada.valores()
       #quem começa a jogar
        if n % (m + 1) == 0:
            print("Você começa!")
            jogador = True
        else:
            print("Computador começa!")
            jogador = False
            

            # algoritmo do jogo     quando o usuario começa a jogar
        if jogador:
            while n > 0:
                print('sua vez de jogar')
               
                usuario = Calculo.usuario_escolhe_jogada(0,n, m)
                n -= usuario
                print('voce tirou', usuario, 'peças.')
                print("tem", n, "peças.")
                # jogador = False
                if n == 0:
                    print("Você ganhou!")
                  
                    break
                else:
                    computador= Calculo.computador_escolhe_jogada(0,n,m) #defnir função do compuatador!
                    n -= computador
                    print('computador tirou', computador, 'peças.')
                    print("tem", n, "peças.")
                    if n == 0:
                        print("Computador ganhou!")
                     
                        break
        # quando o computador começa a jogar
        else:
            while n > 0:    
              
                print(' vez do computa')
               
                computador= Calculo.computador_escolhe_jogada(0,n,m) #defnir função do compuatador!
                print('computador tirou', computador, 'peças.')
                n = n- computador
                print("tem", n, "peças.")
                if n == 0:
                    print("Computador ganhou!")
                   
                    break
                else:
                    print('sua vez de jogar')
                
                    usuario = Calculo.usuario_escolhe_jogada(0,n, m)
                    n =n- usuario
                    print('voce tirou', usuario, 'peças.')
                    print("tem", n, "peças.")
                    if n == 0:
                        print("Você ganhou!")
                        
                        break

  