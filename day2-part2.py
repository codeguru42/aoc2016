import unittest
import sys

class Day2(unittest.TestCase):
  def test1(self):
    instructions = "ULL\nRRDDD\nLURDL\nUUUUD"
    self.assertEqual('5DB3', getBathroomCode(instructions))

  def test2(self):
    instructions = "UU\nRR\nDR\nLLL\nDL"
    self.assertEqual('57CAA', getBathroomCode(instructions))

def getBathroomCode(instructions):
  keypad = [ ['*', '*', '*', '*', '*', '*', '*']
           , ['*', '*', '*', '1', '*', '*', '*']
           , ['*', '*', '2', '3', '4', '*', '*']
           , ['*', '5', '6', '7', '8', '9', '*']
           , ['*', '*', 'A', 'B', 'C', '*', '*']
           , ['*', '*', '*', 'D', '*', '*', '*']
           , ['*', '*', '*', '*', '*', '*', '*']
           ]
  movesx = { 'U': 0 , 'D':0 , 'L':-1, 'R':1 }
  movesy = { 'U':-1 , 'D':1 , 'L': 0, 'R':0 }
  code = []
  x = 1
  y = 3

  for line in instructions.split('\n'):
    if line:
      for c in line:
        x += movesx[c]
        y += movesy[c]

        if keypad[y][x] == '*':
          x -= movesx[c]
          y -= movesy[c]

      code.append(keypad[y][x])

  return ''.join(code)

def main():
  print(getBathroomCode(sys.stdin.read()))

if __name__ == "__main__":
  unittest.main(exit=False)
  main()
