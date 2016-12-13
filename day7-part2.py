import unittest
import re
import sys

class Day7Part1(unittest.TestCase):
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

def main():
  pass

if __name__ == "__main__":
  unittest.main(exit=False)
  main()
