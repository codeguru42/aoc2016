import unittest
import re
import string
import operator

class Day4(unittest.TestCase):
  def test1(self):
    self.assertTrue(isRealRoom("aaaaa-bbb-z-y-x-123[abxyz]"))

  def test2(self):
    self.assertTrue(isRealRoom("a-b-c-d-e-f-g-h-987[abcde]"))

  def test3(self):
    self.assertTrue(isRealRoom("not-a-real-room-404[oarel]"))

  def test4(self):
    self.assertFalse(isRealRoom("totally-real-room-200[decoy]"))

def alphaCount(text):
  counts = dict()
  for c in string.ascii_lowercase:
    counts[c] = 0

  for c in text:
    if c in string.ascii_lowercase:
      counts[c] += 1

  return counts

def isRealRoom(room):
  roomRegEx = '([a-z]+(?:-[a-z]+)*)-([0-9]+)\[([a-z]+)\]'
  m = re.fullmatch(roomRegEx, room)
  if m:
    c = alphaCount(m.group(0))
    sorted_c = sorted(c.items(), key=operator.itemgetter(1), reverse=True)
    letters = [pair[0] for pair in sorted_c[:5]]
    print(letters)
    print(m.groups())
    return ''.join(letters) == m.group(2)
  return False

if __name__ == "__main__":
  unittest.main()
