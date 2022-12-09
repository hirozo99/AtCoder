n = list(map(int, input().split()))

ans = n[0]
for i in range(2):
    ans = n[ans]
print(ans)

