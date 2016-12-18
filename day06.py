import unittest
import io

class Day6Part1Test(unittest.TestCase):
  def test1(self):
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
    message = 'easter'
    self.assertEqual(message, get_message(io.StringIO(data)))

def get_message(data):
  counts = None
  for line in data:
    line = line.strip()
    if counts == None:
      counts = [{} for _ in range(len(line))]
    for i, c in enumerate(line):
      counts[i][c] = counts[i].get(c, 0) + 1

  message = []
  for d in counts:
    maxCount = 0
    for key in d:
      if d[key] > maxCount:
        maxCount = d[key]
        c = key
    message.append(c)
  return ''.join(message)

if __name__ == '__main__':
  unittest.main()
