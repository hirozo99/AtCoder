N = int(input())
A = list(map(int, input().split()))

A.sort()
ans = 0
for i in range(1, N+1):
    if A[i-1] == i:
        ans += 1

if ans == N:
    print("Yes")
else:
    print("No")