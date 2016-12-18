import unittest
import io
import sys

class Day6Part1Test(unittest.TestCase):
  data = '''eedadn
            drvtee
            eandsr
            raavrd
            atevrs
            tsrnev
            sdttsa
            rasrtv
            nssdts
            ntnada
            svetve
            tesnvt
            vntsnd
            vrdear
            dvrsen
            enarar'''

  def test1(self):
    message = 'easter'
    self.assertEqual(message, get_message(io.StringIO(Day6Part1Test.data), select_max))

  def test2(self):
    message = 'advent'
    self.assertEqual(message, get_message(io.StringIO(Day6Part1Test.data), select_min))

def get_message(data, select):
  counts = None
  for line in data:
    line = line.strip()
    if counts == None:
      counts = [{} for _ in range(len(line))]
    for i, c in enumerate(line):
      counts[i][c] = counts[i].get(c, 0) + 1

  message = []
  for d in counts:
    c = select(d)
    message.append(c)
  return ''.join(message)

def select_max(d):
  maxCount = 0
  for key in d:
    if d[key] > maxCount:
      maxCount = d[key]
      c = key
  return c

def select_min(d):
  minCount = sys.maxsize
  for key in d:
    if d[key] < minCount:
      minCount = d[key]
      c = key
  return c

if __name__ == '__main__':
  if unittest.main(exit=False).result.wasSuccessful():
    data = sys.stdin.read()
    print(get_message(io.StringIO(data), select_max))
    print(get_message(io.StringIO(data), select_min))
