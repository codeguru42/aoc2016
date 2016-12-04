import sys

turns = { 'N' : { 'L' : 'W', 'R' : 'E' }
        , 'S' : { 'L' : 'E', 'R' : 'W' }
        , 'E' : { 'L' : 'N', 'R' : 'S' }
        , 'W' : { 'L' : 'S', 'R' : 'N' }
        }

with open(sys.argv[1]) as f:
  north = 0
  east = 0
  currDir = 'N'
  for line in f:
    moves = line.strip().split(',')
    for move in moves:
      move = move.strip()
      currDir = turns[currDir][move[0]]
      blocks = int(move[1:])
      if currDir == 'N':
        north += blocks
      elif currDir == 'S':
        north -= blocks
      elif currDir == 'E':
        east += blocks
      elif currDir == 'W':
        east -= blocks
      print('move: {0}, north: {1}, east: {2}'.format(move, north, east))

  print(abs(north) + abs(east))
