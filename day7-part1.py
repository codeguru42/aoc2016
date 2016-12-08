import unittest
import re

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
  abbaRegex = r'(.)(.)\2\1'
  match = re.search(abbaRegex, s)
  return match and match.group(1) != match.group(2)

def supportsTLS(ip):
  ipABBA = False
  hypernetABBA = False
  ipRegex = re.compile(r'[^[]*')
  hypernetRegex = re.compile(r'\[([^]]*)\]')

  m = ipRegex.match(ip)
  while m:
    print(m.group(0))
    ipABBA = ipABBA or containsABBA(m.group(0))
    print("ip result:", ipABBA)
    m = hypernetRegex.match(ip, m.end())
    if m:
      print(m.group(0))
      hypernetABBA = hypernetABBA or containsABBA(m.group(1))
      print("hypernet result:", hypernetABBA)
      m = ipRegex.match(ip, m.end())

  if m:
    print(m.group(0))

  print("result:", ipABBA and not hypernetABBA)
  return ipABBA and not hypernetABBA

def main():
  pass

if __name__ == "__main__":
  unittest.main(exit=False)
  main()
