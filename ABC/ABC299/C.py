N = int(input())
S = input()

total = 0
ans = 0

for i in range(N):
    if S[i] == "-":
        total = 0
    else:
        total += 1
        ans = max(total, ans)

if ans and "-" in S:
    print(ans)
else:
    print(-1)

