N = int(input())

ans = []
for i in range(N):
    ans.append(input())

for i in range(N-1, -1, -1):
    print(ans[i])