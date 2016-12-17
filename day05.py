import unittest
import hashlib
import itertools

class PasswordTest(unittest.TestCase):
  def test1(self):
    door_id = 'abc'
    password = '18f47a30'
    self.assertEqual(password, get_password(door_id))

  def test2(self):
    door_id = 'abc'
    password_iter = iter(generate_password(door_id))
    self.assertEqual('1', next(password_iter))

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

class BetterPasswordTest(unittest.TestCase):
  def test1(self):
    door_id = 'abc'
    password = '05ace8e3'
    self.assertEqual(password, get_better_password(door_id))

def generate_password(door_id):
  i = 0
  while True:
    m = hashlib.md5()
    indexed_door_id = (door_id + str(i)).encode('utf-8')
    m.update(indexed_door_id)
    md5hash = m.hexdigest()
    if md5hash[:5] == '00000':
      yield md5hash[5]
    i += 1

def get_password(door_id):
  return ''.join(itertools.islice(generate_password(door_id), 8))

if __name__ == "__main__":
  if unittest.main(exit=False).result.wasSuccessful():
    door_id = 'abbhdwsy'
    print(get_password(door_id))
