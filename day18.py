import unittest
import itertools
import sys

class NextRowTest(unittest.TestCase):
  def test1(self):
    row = '..^^.'
    next_row = '.^^^^'
    self.assertEqual(next_row, get_next_row(row))

  def test2(self):
    row = '.^^^^'
    next_row = '^^..^'
    self.assertEqual(next_row, get_next_row(row))

  def test3(self):
    row = '.^^.^.^^^^'
    next_row = '^^^...^..^'
    self.assertEqual(next_row, get_next_row(row))

  def test4(self):
    row = '^^^...^..^'
    next_row = '^.^^.^.^^.'
    self.assertEqual(next_row, get_next_row(row))

class CountSafeTest(unittest.TestCase):
  def test1(self):
    row = '..^^.'
    result = 3
    self.assertEqual(result, count_safe(row))

  def test2(self):
    row = '.^^^^'
    result = 1
    self.assertEqual(result, count_safe(row))

  def test3(self):
    row = '^^..^'
    result = 2
    self.assertEqual(result, count_safe(row))

  def test4(self):
    row = '.^^.^.^^^^'
    result = 3
    self.assertEqual(result, count_safe(row))

def window(seq, n=2):
  it = iter(seq)
  result = tuple(itertools.islice(it, n))
  if len(result) == n:
    yield result
  for elem in it:
    result = result[1:] + (elem,)
    yield result

def get_next_row(row):
  row = '.' + row + '.'
  next_row = []
  for w in window(row, 3):
    if ((w[0] == '^' and w[1] == '^' and w[2] == '.')
      or (w[0] == '.' and w[1] == '^' and w[2] == '^')
      or (w[0] == '^' and w[1] == '.' and w[2] == '.')
      or (w[0] == '.' and w[1] == '.' and w[2] == '^')):
      next_row.append('^')
    else:
      next_row.append('.')
  return ''.join(next_row)

def count_safe(row):
  count = 0
  for t in row:
    if t == '.':
      count += 1
  return count

if __name__ == "__main__":
  if unittest.main(exit=False).result.wasSuccessful():
    row = sys.stdin.readline()
    count = count_safe(row)
    for i in range(40):
      row = get_next_row(row)
      count += count_safe(row)
    print(count)
