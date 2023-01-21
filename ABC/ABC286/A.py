N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))

f = []
s = []

for i in range(P, Q+1):
    f.append(A[i-1])

for i in range(R, S+1):
    s.append(A[i-1])

A[P-1:Q] = s
A[R-1:S] = f
print(*A)

# print(*f)
# print(*s)
