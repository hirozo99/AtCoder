H, W = map(int, input().split())
S_list = [input() for _ in range(H)]

ans = 0
for i in range(H):
    ans += S_list[i].count("#")

print(ans)
