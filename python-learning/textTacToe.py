# tuples are immutable
# lists are similar to arrays
game = [
  [1, 0, 0],
  [1, 0, 0],
  [1, 0, 0]
]

for i in range(len(game)):
  check = []
  for row in game:
    check.append(row[i])

  if check.count(check[0]) == len(check) and check[0] != 0:
    print('winny boi')

def win(current_game):
  for row in game:
    if row.count(row[0]) == len(row) and row[0] != 0:
      print('winner')

def game_board(gmap, p=0, row=0, col=0):
  try:
    print('    a  b  c')
    if p != 0:
      gmap[row][col] = p
    for count, row in enumerate(gmap):
      print(count, row)
    return gmap
  except IndexError as e:
    print('Error: please input row/column as 0, 1, or 2', e)
  except Exception as e:
    print('something went wrong: ', e)

game = game_board(game, p = 1, row = 1, col = 1)

'''
win conditions
horizontally
vertically
diagonally
'''

