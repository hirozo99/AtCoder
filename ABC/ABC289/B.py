N, M = map(int, input().split())
graph = [[] for _ in range(M)]
a = list(map(int, input().split()))

for i in range(M):
    x = a[i]
    y = x + 1
    graph[i].append(y-1)
    graph[i].append(y)

print(graph)

ans = []
for i in range(M-1):
    if graph[i][1] == graph[i+1][0]:
        k = graph[i] + graph[i+1]
        ans.append(k)
    else:
        ans.append(graph[i])
print(ans)

check = []
for i in range(len(ans)):
    check.append(set(ans[i]))

print(check)