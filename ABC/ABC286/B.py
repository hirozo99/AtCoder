N = int(input())
S = list(input())

ans = []
for i in range(N):
    if S[i] == "n" and i < N-1:
        if S[i+1] == "a":
            ans.append(S[i]+"y")
        else:
            ans.append(S[i])
    else:
        ans.append(S[i])
print("".join(ans))