matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
def mapaDasPosições():
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

def jogo(tabuleiro, jogada, simb): #preenche o tabuleiro e verifica se a casa já está preenchida ou se foi digitado número errado
  posicoes = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
  }
  
  if jogada not in posicoes:
    return False

  c, l = posicoes[jogada]

  if matriz[c][l] in 'xo':
    return False

  matriz[c][l] = simb

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
    
    mapaDasPosições()
    cont = 0
    while True:
        jogada = int(input('Sua jogada: '))
        if cont % 2 == 0:
            simb = 'x'
        else:
            simb = 'o'
        
        if not jogo(tabuleiro, jogada, simb):
            print("Jogada Inválida! Tente Novamente!")
            continue
        
        tabuleiro(matriz)
        if temGanhador(tabuleiro, simb):
            print(f'Jogador "{simb}" é o VENCEDOR!')
            break

        cont += 1
        if cont == 9:
            print('Que pena! VELHOU!')
            break

main()

