n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b)
    graph[b-1].append(a)

for (i, j) in enumerate(graph):
    j.sort()
    print(len(j), *j)

# n, m = map(int, input().split())
# a = [ None ] * m
# b = [ None ] * m
# for i in range(m):
#     a[i], b[i] = map(int, input().split())
#
# g = [ [] for i in range(n+1)]
# for i in range(m):
#     g[a[i]].append(b[i])
#     g[b[i]].append(a[i])
#
# for i, j in enumerate(g):
#     j.sort()
#     print(len(j), *j)