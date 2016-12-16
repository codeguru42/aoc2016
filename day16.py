import unittest

class DragonTest(unittest.TestCase):
  def test1(self):
    data = "1"
    expected = "100"
    self.assertEqual(expected, dragon(data))

  def test2(self):
    data = "0"
    expected = "001"
    self.assertEqual(expected, dragon(data))

  def test3(self):
    data = "11111"
    expected = "11111000000"
    self.assertEqual(expected, dragon(data))

  def test4(self):
    data = "111100001010"
    expected = "1111000010100101011110000"
    self.assertEqual(expected, dragon(data))

  def test5(self):
    data = "10000"
    expected = "10000011110"
    self.assertEqual(expected, dragon(data))

  def test6(self):
    data = "10000011110"
    expected = "10000011110010000111110"
    self.assertEqual(expected, dragon(data))

class ChecksumTest(unittest.TestCase):
  def test1(self):
    data = "110010110100"
    expected = "100"
    self.assertEqual(expected, checksum(data))

  def test2(self):
    data = "10000011110010000111"
    expected = "01100"
    self.assertEqual(expected, checksum(data))

class ChecksumStepTest(unittest.TestCase):
  def test1(self):
    data = "110010110100"
    expected = "110101"
    self.assertEqual(expected, checksumStep(data))

  def test2(self):
    data = "110101"
    expected = "110101"
    self.assertEqual(expected, checksumStep(data))

  def test3(self):
    data = "10000011110010000111"
    expected = "0111110101"
    self.assertEqual(expected, checksumStep(data))

  def test4(self):
    data = "0111110101"
    expected = "01100"
    self.assertEqual(expected, checksumStep(data))

class FillDiskTest(unittest.TestCase):
  def test1(self):
    initial = "10000"
    disk_size = 20
    expected = "10000011110010000111"
    self.assertEqual(expected, fill_disk(disk_size, initial))

class BitwiseNotTest(unittest.TestCase):
  def test1(self):
    bits = "0"
    expected = "1"
    self.assertEqual(expected, bitwise_not(bits))

  def test2(self):
    bits = "1"
    expected = "0"
    self.assertEqual(expected, bitwise_not(bits))

  def test3(self):
    bits = "11111"
    expected = "00000"
    self.assertEqual(expected, bitwise_not(bits))

  def test4(self):
    bits = "111100001010"
    expected = "000011110101"
    self.assertEqual(expected, bitwise_not(bits))

def dragon(a):
  b = bitwise_not(a[::-1])
  return a + "0" + b

def bitwise_not(bits):
  def bit_not(bit):
    if bit == '0':
      return '1'
    elif bit == '1':
      return '0'

  return ''.join(map(bit_not, bits))

def checksumStep(data):
  pass

def checksum(data):
  pass

def fill_disk(size, initial):
  pass

if __name__ == "__main__":
  unittest.main()
