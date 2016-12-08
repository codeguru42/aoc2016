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

  def test5(self):
    s = 'abba'
    self.assertTrue(containsABBA(s))

  def test6(self):
    s = 'abcd'
    self.assertFalse(containsABBA(s))

  def test7(self):
    s = 'aaaa'
    self.assertFalse(containsABBA(s))

  def test8(self):
    s = 'ioxxo'
    self.assertTrue(containsABBA(s))

  def test9(self):
    s = 'bddb'
    self.assertTrue(containsABBA(s))

  def test10(self):
    s = 'xyyx'
    self.assertTrue(containsABBA(s))

  def test11(self):
    s = 'qrst'
    self.assertTrue(containsABBA(s))

def containsABBA(s):
  pass

def supportsTLS(ip):
  pass

def main():
  pass

if __name__ == "__main__":
  unittest.main(exit=False)
  main()
