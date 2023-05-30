S = input()
N = len(S)
V = []
for i in range(0, N):
    V.append(S[i:N] + S[0:i])
print(min(V))
print(max(V))