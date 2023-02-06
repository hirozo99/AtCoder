N,M = map(int, input().split())
Adj = [[] * N for _ in range(N)]

for _ in range(M):
  A,B = map(int, input().split())
  Adj[A-1].append(B-1)
  Adj[B-1].append(A-1)

def dfs(x):
  for y in Adj[x]:
    if not visited[y]:
      visited[y] = True
      dfs(y)

visited = [False] * N
cyc = 0

for i in range(N):
  if not visited[i]:
    visited[i] = True
    dfs(i)
    cyc += 1

print(M - N + cyc)