S = list(input())

ans = []
for i in range(1, len(S)+1):
    if S[-i] == "6":
        ans.append("9")
    elif S[-i] == "9":
        ans.append("6")
    else:
        ans.append(S[-i])

print("".join(ans))