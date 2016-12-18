import unittest

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
    self.assertEqual(message, get_message(data))

if __name__ == '__main__':
  unittest.main()
