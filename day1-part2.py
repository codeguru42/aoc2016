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
  visited = set()
  for line in f:
    moves = line.strip().split(',')
    for move in moves:
      print('move: {0}, north: {1}, east: {2}'.format(move, north, east))
      move = move.strip()
      currDir = turns[currDir][move[0]]
      blocks = int(move[1:])
      if currDir == 'N':
        for north in range(north, north + blocks):
          if (north, east) in visited:
            print(abs(north) + abs(east))
            exit(0)
          visited.add((north, east))
          north += 1
      elif currDir == 'S':
        for north in range(north, north - blocks, -1):
          if (north, east) in visited:
            print(abs(north) + abs(east))
            exit(0)
          visited.add((north, east))
          north -= 1
      elif currDir == 'E':
        for east in range(east, east + blocks):
          if (north, east) in visited:
            print(abs(north) + abs(east))
            exit(0)
          visited.add((north, east))
          east += 1
      elif currDir == 'W':
        for east in range(east, east - blocks, -1):
          if (north, east) in visited:
            print(abs(north) + abs(east))
            exit(0)
          visited.add((north, east))
          east -= 1
