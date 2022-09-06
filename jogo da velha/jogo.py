#matriz para ser preenchida pelos jogadores
matriz = [['', '', ''], ['', '', ''], ['', '', '']]

def tabuleiro():
  for l in range(0, 3):
    for c in range(0, 3):
      print(f'[{matriz[l][c]:^3}]', end=' ')
    print()
  print('~' * 30)

def jogar():
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
      
      if jogada < 0 or jogada > 9:
        print('Erro!!! Tente novamente!')

def ganhou():
  
  #verificação na horizontal
  if matriz[0][0] == simb and matriz[0][1] == simb and matriz[0][2] == simb:
    return True
  
  if matriz[1][0] == simb and matriz[1][1] == simb and matriz[1][2] == simb:
    return True

  if matriz[2][2] == simb and matriz[2][1] == simb and matriz[2][2] == simb:
    return True

  #verificação na vertical
  if matriz[0][0] == simb and matriz[1][0] == simb and matriz[2][0] == simb:
    return True

  if matriz[0][1] == simb and matriz[1][1] == simb and matriz[2][1] == simb:
    return True

  if matriz[0][2] == simb and matriz[1][2] == simb and matriz[2][2] == simb:
    return True

  #verificação na diagonal
  if matriz[0][0] == simb and matriz[1][1] == simb and matriz[2][2] == simb:
    return True

  if matriz[2][0] == simb and matriz[1][1] == simb and matriz[0][2] == simb:
    return True

#mapa das posições a serem marcadas
print('~' * 30)
print(f'{"JOGO DA VELHA":^30}')
print('~' * 30)

mapa = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('MAPA DAS POSIÇÕES')
for l in range(0, 3):
  for c in range(0, 3):
    print(f'[{mapa[l][c]:^3}]', end=' ')
  print()
print('~' * 30)

#aqui começa de fato o jogo
cont = 0
while True:
  if cont % 2 == 0:
    simb = 'o'
  else:
    simb = 'x'

  jogada = int(input(f'Jogador {simb}: '))
  jogar()
  tabuleiro()
  cont += 1
  
  if ganhou():
    print(f'Jogador "{simb}" é o VENCEDOR!!!')
    break
  if cont == 9:
    print('VELHOU!!!')
    break