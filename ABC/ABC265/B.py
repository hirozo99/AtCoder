N, M, T = map(int, input().split())
A = [0] + list(map(int, input().split()))

bonus = [0] * (N+1)
for i in range(M):
    X, Y = map(int, input().split())
    bonus[X] = Y

for i in range(1, N):
    T -= A[i]
    if T <= 0:
        print("No")
        exit()
    T += bonus[i+1]
print("Yes")