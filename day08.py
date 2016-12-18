import unittest

class ScreenTest(unittest.TestCase):
  def setUp(self):
    self.screen = screen(7, 3)

  def testRect(self):
    self.screen.rect(3, 2)
    expected = '###....\n###....\n.......'
    self.assertEquals(expected, str(screen))

if __name__ == "__main__":
  if unittest.main(exit=False).result.wasSuccessful():
    pass
