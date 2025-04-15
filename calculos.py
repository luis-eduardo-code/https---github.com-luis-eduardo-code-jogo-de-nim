class Calculo:
    """criar uma funcao para jogador ou computador tirar peças"""

    def usuario_escolhe_jogada(self, n, m):
        """usuario escolhe jogada"""
        valor_retirado = 0  # variavel para armazenar o valor retirado
       
        # loop para verificar se o valor retirado é valido
        while True:
            try:
                valor_retirado = int(input('Quantas peças você vai tirar? '))
                if 1 <= valor_retirado <= m:
                    return valor_retirado  # retorna o valor retirado
                else:
                    print(f"Oops! Você só pode tirar entre 1 e {m} peças. Tente de novo.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")

    def computador_escolhe_jogada(self, n, m):
        """computador escolhe jogada"""
        valor_retirado = 0
        # loop para verificar se o valor retirado é valido
        if n <= m:
            valor_retirado = n
        elif n % (m + 1) == 0:
            valor_retirado = m
        else:
            valor_retirado = n % (m + 1)
        return valor_retirado # VARIAVEL RETIRADOAI SOBRA UM NUMERO DE PEÇAS QUE É MULTIPLO DE (M+1)
