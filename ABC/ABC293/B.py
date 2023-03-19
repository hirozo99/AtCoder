N = int(input())
A = list(map(int, input().split()))

called = [0] * N

for i in range(N):
    if not called[i]:



for i in range(1, N):
    if A[i-1] in check:
        check.remove(A[i-1])
        print(i, check)
    else:
        print(i, check)
        pass

print(check)