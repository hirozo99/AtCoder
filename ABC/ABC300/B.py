def solve():
    H, W = map(int, input().split())
    A = [None] * H
    for i in range(H):
        A[i] = list(input())

    B = [None] * H
    for i in range(H):
        B[i] = list(input())

    for s in range(H):
        for t in range(W):
            for i in range(H):
                A[i] = A[i][1:] + [A[i][0]]
            if A == B:
                return True
        A = A[1:] + [A[0]]
    return False

print("Yes" if solve() else "No")