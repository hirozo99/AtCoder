H, W = map(int, input().split())
A = []
B = [[] for _ in range(W)]
for i in range(H):
    A.append(input().split())
for i in range(W):
    for j in range(H):
        B[i].append(A[j][i])

for i in range(W):
    print(" ".join(B[i]))