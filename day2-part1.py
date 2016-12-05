import unittest

class Day2(unittest.TestCase):
  def test(self):
    instructions = "ULL\nRRDDD\nLURDL\nUUUUD"
    self.assertEqual('1985', getBathroomCode(instructions))

def getBathroomCode(instructions):
  moves = {'U':-3, 'D':+3, 'L':-1, 'R':+1}

  for line in instructions.split('\n'):
    print(line)

def main():
  pass

if __name__ == "__main__":
  unittest.main(exit=False)
  main()
