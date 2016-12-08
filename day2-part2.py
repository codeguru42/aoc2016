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
  movesx = { 'U': 0 , 'D':0 , 'L':-1, 'R':1 }
  movesy = { 'U':-1 , 'D':1 , 'L': 0, 'R':0 }
  code = []
  x = 1
  y = 1

  for line in instructions.split('\n'):
    if line:
      for c in line:
        x += movesx[c]
        y += movesy[c]

        if x < 0 or x > 2:
          x -= movesx[c]

        if y < 0 or y > 2:
          y -= movesy[c]

      code.append(3*y + x + 1)

  return ''.join(map(str, code))

def main():
  print(getBathroomCode(sys.stdin.read()))

if __name__ == "__main__":
  unittest.main(exit=False)
  main()
