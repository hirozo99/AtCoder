from math import sqrt
N = int(input())
x = [0]*N
y = [0]*N
for i in range(N):
    x[i],y[i] = map(int,input().split())
ans = 0
for i in range(N):
    for j in range(i+1,N):
        X = x[i]-x[j]
        Y = y[i]-y[j]
        ans = max(ans,sqrt(X*X+Y*Y))
print(ans)
