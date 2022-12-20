H, W = map(int, input().split())
c = [input() for i in range(H)]

n = []
for w in range(W):
    count = 0
    for h in range(H):
        if c[h][w] == "#":
            count += 1
    n.append(count)
print(*n)