import sys

def is_triangle(a, b, c):
  return a + b > c and a + c > b and b + c > a

lines = sys.stdin.readlines()
count = 0
for line in lines:
  data = line.split()
  if is_triangle(int(data[0]), int(data[1]), int(data[2])):
    count += 1
print(count)

count = 0
for group in zip(*[iter(lines)] * 3):
  triangles = list(map(str.split, group))
  print("triangles:", triangles)
  for i in range(3):
    print(triangles[0][i], triangles[1][i], triangles[2][i])
    if is_triangle(triangles[0][i], triangles[1][i], triangles[2][i]):
      count += 1
print(count)
