from collections import defaultdict

N, M = map(int, input().split())

U = ["$"]
V = ["$"]
for i in range(M):
    u, v = map(int, input().split())
    U.append(u)
    V.append(v)



def count_connected_components(N, M, edges):
    graph = defaultdict(list)
    # グラフを構築する
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # 頂点を訪問したかどうかを示す配列
    visited = [False] * (N + 1)
    count = 0

    # 頂点を訪問する再帰関数
    def dfs(v):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor)

    # 全ての頂点を訪問する
    for v in range(1, N + 1):
        if not visited[v]:
            dfs(v)
            count += 1

    return count

print(count_connected_components(N, M, edges))

