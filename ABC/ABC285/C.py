S = ["$"] + list(input())

def q_num():
    ans = 0
    for i in range(1, len(S)):
        ans += (26 ** (i-1)) * (ord(S[-i])-64)
    return ans

print(q_num())


