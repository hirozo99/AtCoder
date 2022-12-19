H, W = map(int, input().split())

check_list = []
for _ in range(H):
    c = list(input())
    check_list.append(c)

ans = []
for w in range(W):
    count = 0
    for h in range(H):
        if check_list[h][w] == "#":
            count += 1
    ans.append(count)
print(*ans)