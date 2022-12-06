def solve(A, B, C, X):
    q = X // (A + C)
    r = X % (A + C)
    return (q * A + min(A, r)) * B

A, B, C, D, E, F, X = map(int, input().split())

takahashi = solve(A, B, C, X)
aoki = solve(D, E, F, X)

if takahashi > aoki:
    print("Takahashi")
elif takahashi < aoki:
    print("Aoki")
else:
    print("Draw")
