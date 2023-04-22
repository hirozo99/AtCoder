N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

r = 0
winner = 0
if T in C:
    for i in range(N):
        if C[i] == T and r < R[i]:
            r = R[i]
            winner = i + 1
else:
    for i in range(N):
        if C[0] == C[i] and r < R[i]:
            r = R[i]
            winner = i + 1

print(winner)
