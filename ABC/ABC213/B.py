N = int(input())
A = list(map(int, input().split()))

B = sorted(A)
for i in range(N):
    if A[i] == B[-2]:
        print(i+1)
