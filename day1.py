with open("day1.txt") as f:
  north = 0
  east = 0
  for line in f:
    moves = line.strip().split(',')
    print(moves)
