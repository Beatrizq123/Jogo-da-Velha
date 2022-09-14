matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
def mapaDasPosicoes():
    print("~" * 30)
    print(f'{"JOGO DA VELHA":^30}')
    print("~" * 30)
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for c in range(0, 3):
        for l in range(0, 3):
          print(f'[{matriz[c][l]}]', end='')
        print()
    print("~" * 30)

def tabuleiro(matriz): #cria o tabuleiro vazio
    
  for c in range(0, 3):
    for l in range(0, 3):
      print(f'[{matriz[c][l]}]', end='')
    print()

def preenchimento(tabuleiro, jogada, simb): #preenche as casas com as jogadas
    if jogada == 1:
        matriz[0][0] = simb
    if jogada == 2:
        matriz[0][1] = simb
    if jogada == 3:
        matriz[0][2] = simb
    if jogada == 4:
        matriz[1][0] = simb
    if jogada == 5:
        matriz[1][1] = simb
    if jogada == 6:
        matriz[1][2] = simb
    if jogada == 7:
        matriz[2][0] = simb
    if jogada == 8:
        matriz[2][1] = simb
    if jogada == 9:
        matriz[2][2] = simb

def tenteDeNovo(tabuleiro, jogada, simb): #caso a casa esteja preenchida ou o jogador digite um número errado
    posicoes = {1: matriz[0][0],
                2: matriz[0][1],
                3: matriz[0][2],
                4: matriz[1][0],
                5: matriz[1][1],
                6: matriz[1][2],
                7: matriz[2][0],
                8: matriz[2][1],
                9: matriz[2][2]
    }

    if jogada < 0 or jogada > 9:
        return True
       
def temGanhador(tabuleiro, simb): #verifica se tem ganhador
    #comparaçõpes na horizontal
    if matriz[0][0] == simb and matriz[0][1] == simb and matriz[0][2] == simb:
        return True
    if matriz[1][0] == simb and matriz[1][1] == simb and matriz[1][2] == simb:
        return True
    if matriz[2][0] == simb and matriz[2][1] == simb and matriz[2][2] == simb:
        return True
    #comparações na vertical
    if matriz[0][0] == simb and matriz[1][0] == simb and matriz[2][0] == simb:
        return True
    if matriz[0][1] == simb and matriz[1][1] == simb and matriz[2][1] == simb:
        return True
    if matriz[0][2] == simb and matriz[1][2] == simb and matriz[2][2] == simb:
        return True
    #comparações na diagonal
    if matriz[0][0] == simb and matriz[1][1] == simb and matriz[2][2] == simb:
        return True
    if matriz[2][0] == simb and matriz[1][1] == simb and matriz[0][2] == simb:
        return True

def main(): #jogo
    
    mapaDasPosicoes()
    cont = 0
    while True:
        jogada = int(input('Sua jogada: '))
        if cont % 2 == 0:
            simb = 'x'
        else:
            simb = 'o'
        preenchimento(tabuleiro, jogada, simb)
        tabuleiro(matriz)
        if tenteDeNovo(tabuleiro, jogada, simb):
            print("Jogada Inválida! Tente Novamente!")
            continue
        
        if temGanhador(tabuleiro, simb):
            print(f'Jogador "{simb}" é o VENCEDOR!')
            break

        cont += 1
        if cont == 9:
            print('Que pena! VELHOU!')
            break

main()