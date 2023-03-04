N = int(input())

a = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(i+1):
        if j== 0 or j == i:
            a[i][j] = 1
        else:
            a[i][j] = a[i-1][j-1] + a[i-1][j]

for i in range(N):
    print(*a[i][:i+1])