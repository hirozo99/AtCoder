N, M = map(int, input().split())
E = []
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    E.append((a, b))
# ------------------
p = [-1] * (N + 1)
def root(x):
  if p[x] < 0:
    return x
  p[x] = root(p[x])
  return p[x]
 
def unite(x, y):
  x = root(x)
  y = root(y)
  if x == y:
    return
  p[x] += p[y]
  p[y] = x

def size(x):
  x = root(x)
  return -p[x]
# ------------------
cnt = 0
for a, b in E:
    if root(a) != root(b):
        unite(a, b)
    else:
        cnt += 1

print(cnt)