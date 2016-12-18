import unittest

class ScreenTest(unittest.TestCase):
  def setUp(self):
    self.screen = screen(7, 3)

  def testRect(self):
    self.screen.rect(3, 2)
    expected = '###....\n###....\n.......'
    self.assertEquals(expected, str(self.screen))

class screen:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.screen = [['.'] * width for _ in range(height)]

  def __str__(self):
    return '\n'.join([''.join(c) for c in self.screen])

  def rect(self, width, height):
    for i in range(width):
      for j in range(height):
        self.screen[j][i] = '#'

if __name__ == "__main__":
  if unittest.main(exit=False).result.wasSuccessful():
    pass
