s = input()

judge = len(set(s))
if judge == 1:
    print(1)
elif judge == 2:
    print(3)
elif judge == 3:
    print(6)
print(set(s))

# 解説の実装例
S = input()
ans = 3
if S[0] == S[1] and S[1] == S[2]:
    ans = 1
elif S[0] != S[1] and S[1] != S[2] and S[0] != S[2]:
    ans = 6
print(ans)
