import unittest

class DragonTest(unittest.TestCase):
  def test1(self):
    binary = "1"
    expected = "100"
    self.assertEqual(expected, dragon(binary))

  def test2(self):
    binary = "0"
    expected = "001"
    self.assertEqual(expected, dragon(binary))

  def test3(self):
    binary = "11111"
    expected = "11111000000"
    self.assertEqual(expected, dragon(binary))

  def test4(self):
    binary = "111100001010"
    expected = "1111000010100101011110000"
    self.assertEqual(expected, dragon(binary))

if __name__ == "__main__":
  unittest.main()
