P = list(map(int, input().split()))

ans = []
for i in range(26):
    ans.append(chr(96+P[i]))

print("".join(ans))