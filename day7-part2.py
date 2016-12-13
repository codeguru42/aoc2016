import unittest
import re
import sys

class Day7Part2(unittest.TestCase):
  def test1(self):
    ip = "aba[bab]xyz"
    self.assertTrue(supportsSSL(ip))

  def test2(self):
    ip = "xyx[xyx]xyx"
    self.assertFalse(supportsSSL(ip))

  def test3(self):
    ip = "aaa[kek]eke"
    self.assertTrue(supportsSSL(ip))

  def test4(self):
    ip = "zazbz[bzb]cdb"
    self.assertTrue(supportsSSL(ip))

  def test5(self):
    supernet = "aba"
    self.assertTrue(hasABA(supernet))

  def test6(self):
    supernet = "xyx"
    self.assertTrue(hasABA(supernet))

  def test7(self):
    supernet = "aaa"
    self.assertFalse(hasABA(supernet))

  def test8(self):
    supernet = "zazbz"
    self.assertTrue(hasABA(supernet))

def hasABA(supernet):
  supernet_pattern = r'(.).\1'
  return re.search(supernet_pattern, supernet)

def main():
  pass

if __name__ == "__main__":
  unittest.main(exit=False)
  main()
