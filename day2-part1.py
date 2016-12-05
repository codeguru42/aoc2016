import unittest
import sys

class Day2(unittest.TestCase):
  def test1(self):
    instructions = "ULL\nRRDDD\nLURDL\nUUUUD"
    self.assertEqual('1985', getBathroomCode(instructions))

  def test2(self):
    instructions = "UU\nRR\nDR\nLLL\nDL"
    self.assertEqual('23647', getBathroomCode(instructions))

def getBathroomCode(instructions):
  moves = {'U':-3, 'D':+3, 'L':-1, 'R':+1}
  code = []
  pos = 5

  for line in instructions.split('\n'):
    for c in line:
      pos += moves[c]
      if pos < 1 or pos > 9:
        pos -= moves[c]
    code.append(pos)

  return ''.join(map(str, code))

def main():
  print(getBathroomCode(sys.stdin.read()))

if __name__ == "__main__":
  unittest.main(exit=False)
  main()
