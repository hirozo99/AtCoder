H, W = map(int, input().split())

array = []
for i in range(H):
    A = list(map(int, input().split()))
    array.append(A)

ans = [[] for i in range(H)]
for h in range(H):
    for w in range(W):
        if array[h][w] == 0:
            ans[h].append(".")
        else:
            ans[h].append(chr(64+array[h][w]))

for i in range(H):
    print("".join(ans[i]))