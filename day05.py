import unittest
import hashlib

class MD5Test(unittest.TestCase):
  def setUp(self):
    self.m = hashlib.md5()

  def test1(self):
    data = 'abc3231929'.encode('utf-8')
    self.m.update(data)
    result = self.m.hexdigest()
    self.assertEqual('00000', result[:5])

  def test2(self):
    data = 'abc5017308'.encode('utf-8')
    self.m.update(data)
    result = self.m.hexdigest()
    self.assertEqual('00000', result[:5])

  def test3(self):
    data = 'abc5278568'.encode('utf-8')
    self.m.update(data)
    result = self.m.hexdigest()
    self.assertEqual('00000', result[:5])

if __name__ == "__main__":
  unittest.main()
