import unittest
import itertools

class NextRowTest(unittest.TestCase):
  def test1(self):
    row = '.^^^^'
    next_row = '^^..^'
    self.assertEqual(next_row, get_next_row(row))

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

if __name__ == "__main__":
  if unittest.main(exit=False).result.wasSuccessful():
    pass
