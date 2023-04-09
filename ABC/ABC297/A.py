N, D = map(int, input().split())
T = list(map(int, input().split()))

for i in range(N-1):
    if T[i+1]-T[i] <= D:
        ans = T[i+1]
        print(ans)
        exit()
    else:
        pass
print(-1)
