import unittest

def alphaCount(text):
  counts = dict()
  for c in string.ascii_lowercase:
    counts[c] = 0

  for c in text:
    counts[c] += 1

  return counts

if __name__ == "__main__":
  unittest.main()
