n = int(input())

ans = []
for _ in range(n):
    p, q = map(int, input().split())
    ans.append(q/p)

print(sum(ans))
