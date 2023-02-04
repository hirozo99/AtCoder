from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def adjacencyList(self, vertex):
        return self.graph[vertex]


n, m = map(int, input().split())
g = Graph(n)
for i in range(m):
    u, v = map(int, input().split())
    g.addEdge(u, v)

edge = []
for i in range(n+1):
    edge.append(g.adjacencyList(i))

print(edge)

for i in range()

# 頂点数:n
# edge[i]:頂点iと辺で結ばれる頂点の集合
# 遷移元の頂点
parent=[-1]*n
# 閉路に含まれる辺の集合
loop =set()
# 既に探索した頂点か
come=[False]*n

def dfs(x,last=-1):
    if last!=-1:
        parent[x]=last
    come[x]=True
    for i in edge[x]:
        if i ==last:continue
        if come[i]:
            now=x
            loop.add((now,i))
            loop.add((i,now))
            while now!=i:
                loop.add((now,parent[now]))
                loop.add((parent[now],now))
                now=parent[now]
            return True
        else:
            if dfs(i,x):
                return True
    return False

print(dfs(0))
