N = int(input())
S = ["$"] + list(input())

ans = 0
for i in range(1, N+1):
    if S[i-1] != S[i]:
        ans += 1

if ans == N:
    print("Yes")
else:
    print("No")