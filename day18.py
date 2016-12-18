import unittest

class NextRowTest(unittest.TestCase):
  def test1(self):
    row = '.^^^^'
    next_row = '^^..^'
    self.assertEqual(next_row, get_next_row(row))

if __name__ == "__main__":
  if unittest.main(exit=False).result.wasSuccessful():
    pass
