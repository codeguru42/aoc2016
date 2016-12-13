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
    self.assertTrue(getABA(supernet))

  def test6(self):
    supernet = "xyx"
    self.assertTrue(getABA(supernet))

  def test7(self):
    supernet = "aaa"
    self.assertFalse(getABA(supernet))

  def test8(self):
    supernet = "zazbz"
    self.assertTrue(getABA(supernet))

  def test9(self):
    aba = "aba"
    hypernet = "bab"
    self.assertTrue(hasBAB(hypernet, aba))

  def test10(self):
    aba = "xyx"
    hypernet = "xyx"
    self.assertFalse(hasBAB(hypernet, aba))

  def test11(self):
    aba = "eke"
    hypernet = "kek"
    self.assertTrue(hasBAB(hypernet, aba))

  def test12(self):
    aba = "zbz"
    hypernet = "bzb"
    self.assertTrue(hasBAB(hypernet, aba))

def getABA(supernet):
  supernet_pattern = r'(.)(.)\1'
  m = re.search(supernet_pattern, supernet)
  if m and m.group(1) != m.group(2):
    return m.group(0)
  return None

def main():
  pass

if __name__ == "__main__":
  unittest.main(exit=False)
  main()
