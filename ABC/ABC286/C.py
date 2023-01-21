N, A, B = map(int, input().split())
S = input()
ans = 0


if not S[:N] == S[0:]:
    if len(S) > 1:
        S = S[1:] +S[0]
        ans += A

else:
    print(0)