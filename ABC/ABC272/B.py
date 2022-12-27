from itertools import combinations
N, M = map(int, input().split())

s = set()
for m in range(M):
  a = list(map(int, input().split()))
  x = a[1:]
  for i in combinations(x, 2):
    s.add(i)
  # print(len(s))
  # print(s)
if len(s) == N * (N - 1) / 2:
  print("Yes")
else:
  print("No")