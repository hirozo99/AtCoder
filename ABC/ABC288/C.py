n, m = map(int, input().split())

A_list = []
B_list = []
for i in range(m):
    A, B = map(int, input().split())
    A_list.append(A)
    B_list.append(B)

print(A_list, B_list)
pair = [[A_list[i], B_list[i]] for i in range(m)]
print(pair)
pair.sort()
print(pair)


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

dfs(0)