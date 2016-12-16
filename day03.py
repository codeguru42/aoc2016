import sys

def is_triangle(a, b, c):
  return a + b > c and a + c > b and b + c > a

count = 0
for line in sys.stdin:
  data = line.split()
  if is_triangle(int(data[0]), int(data[1]), int(data[2])):
    count += 1
print(count)
