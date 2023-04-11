N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(N):
    if A[i] == max(A):
        for j in range(K):
            if i+1 == B[j]:
                print("Yes")
                exit()

print("No")