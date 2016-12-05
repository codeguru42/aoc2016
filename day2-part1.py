import unittest

class Day2(unittest.TestCase):
  def test(self):
    instructions = "ULL\nRRDDD\nLURDL\nUUUUD"
    self.assertEqual('1985', getBathroomCode(instructions))

def main():
  pass

if __name__ == "__main__":
  unittest.main(exit=False)
  main()
