import unittest

class Day7Part1(unittest.TestCase):
  def test1(self):
    ip = "abba[mnop]qrst"
    self.assertTrue(supportsTLS(ip))

  def test2(self):
    ip = "abcd[bddb]xyyx"
    self.assertTrue(supportsTLS(ip))

  def test3(self):
    ip = "aaaa[qwer]tyui"
    self.assertFalse(supportsTLS(ip))

  def test4(self):
    ip = "ioxxoj[asdfgh]zxcvbn"
    self.assertTrue(supportsTLS(ip))

def main():
  pass

if __name__ == "__main__":
  unittest.main(exit=False)
  main()
