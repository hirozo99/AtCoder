N = int(input())

ans = []
for i in range(N):
    ans.append(input())

for i in range(N):
    print(ans[-(i + 1)])