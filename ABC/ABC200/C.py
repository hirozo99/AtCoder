N = int(input())
A = list(map(int, input().split()))

R = [x % 200 for x in A]
cnt = [0] * 200

ans = 0
for r in R:
    ans += cnt[r]
    cnt[r] += 1

print(ans)