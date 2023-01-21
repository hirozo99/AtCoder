N = int(input())
A = list(map(int, input().split()))

P = 0
base = [0]*4

for i in range(N):
    base[0] = 1
    for j in range(4):
        if base[j] == 1:
            base[j] = base[A[i]]