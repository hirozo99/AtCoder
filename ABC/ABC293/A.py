S = [0] + list(input())

for i in range(1, len(S)//2 + 1):
    x = 0
    x = S[2*i-1]
    S[2*i-1] = S[2*i]
    S[2*i] = x

print("".join(S[1:]))