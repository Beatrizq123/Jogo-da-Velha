def playing(position, gameboard, symbol): #preenche o tabuleiro e verifica se a casa já está preenchida ou se foi digitado número errado
  mapping_positions = {
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

  if position not in mapping_positions:
    return False

  row, col = mapping_positions[position]

  if gameboard[row][col] in 'X0':
    return False

  gameboard[row][col] = symbol

  return True

def show_gameboard(gameboard): #cria o tabuleiro
  for r in range(3):
    for c in range(3):
      print(f'[{gameboard[r][c]}]', end=' ')
    print('\n')

def has_winner(gameboard, symbol): #verifica se tem vencedor
  #horizontal
  if gameboard[0][0] == symbol and gameboard[0][1] == symbol and gameboard[0][2] == symbol:
    return True
  if gameboard[1][0] == symbol and gameboard[1][1] == symbol and gameboard[1][2] == symbol:
    return True
  if gameboard[2][0] == symbol and gameboard[2][1] == symbol and gameboard[2][2] == symbol:
    return True
  #vertical
  if gameboard[0][0] == symbol and gameboard[1][0] == symbol and gameboard[2][0] == symbol:
    return True
  if gameboard[0][1] == symbol and gameboard[1][1] == symbol and gameboard[2][1] == symbol:
    return True
  if gameboard[0][2] == symbol and gameboard[1][2] == symbol and gameboard[2][2] == symbol:
    return True
  #diagonal
  if gameboard[0][0] == symbol and gameboard[1][1] == symbol and gameboard[2][2] == symbol:
    return True
  if gameboard[2][0] == symbol and gameboard[1][1] == symbol and gameboard[0][2] == symbol:
    return True

def main(): #jogo
  gameboard = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
  count_playing = 0

  while count_playing >= 0 and count_playing < 9:
    symbol = 'X' if count_playing % 2 == 0 else '0'
    position = int(input('Digite uma posicao de 1-9: '))
    
    if not playing(position, gameboard, symbol):
      print('Jogada invalida: Jogue um valor que ainda nao foi jogado entre 1-9.')
      continue

    show_gameboard(gameboard)

    if has_winner(gameboard, symbol): #falta fazer
      print(f'Player {symbol} is the WINNER!')
      break

    count_playing += 1
    
    if count_playing == 9:
      print('Opps, GAME OVER!')

main()