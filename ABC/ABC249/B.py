def judge():
    S = input()
    b1 = not S.islower()
    b2 = not S.isupper()
    b3 = len(S) == len(set(S))
    return b1 and b2 and b3


print("Yes" if judge() else "No")