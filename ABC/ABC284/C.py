N, M = map(int, input().split())
visited = [False for _ in range(N)]
from collections import defaultdict
uv = defaultdict(list)
for i in range(M):
    u, v = map(int, input().split())
    uv[u-1].append(v-1)
    uv[v-1].append(u-1)
def dfs(now, ans=0):
    next = uv[now]
    if next == []:
        ans = 1
    for i in next:
        if visited[i]:
            continue
        else:
            visited[i] = True
            ans += 1
            dfs(i)
    return ans
ans = 0
for i in range(N):
    ans += dfs(i)
print(ans)