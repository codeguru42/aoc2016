import unittest
import re
import string
import operator
import sys

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

roomRegEx = '([a-z]+(?:-[a-z]+)*)-([0-9]+)\[([a-z]+)\]'
def isRealRoom(room):
  m = re.fullmatch(roomRegEx, room)
  if m:
    c = alphaCount(m.group(1))
    sorted_c = sorted(c.items(), key=lambda x : (-x[1], x[0]))
    letters = [pair[0] for pair in sorted_c[:5]]
    checksum = ''.join(letters)
    return checksum == m.group(3)
  return False

def main():
  lines = sys.stdin.readlines()
  rooms = filter(lambda line : isRealRoom(line.strip()), lines)
  matches = map(lambda room : re.fullmatch(roomRegEx, room.strip()), rooms)
  ids = [int(m.group(2)) for m in matches]
  print(sum(ids))

if __name__ == "__main__":
  unittest.main(exit=False)
  main()
