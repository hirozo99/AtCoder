N, P = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(N):
    if P > a[i]:
        ans += 1
print(ans)