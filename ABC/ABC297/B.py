S = ["$"] + list(input())

a = 0
for i, x in enumerate(S):
    if a == 0:
        if x == "B":
            b1 = i
            a += 1
    elif a == 1:
        if x == "B":
            b2 = i

b = 0
for i in range(1, 9):
    if b == 0:
        if S[i] == "R":
            k1 = i
            b += 1
    else:
        if S[i] == "R":
            k2 = i
r = 0
for i in range(1, 9):
    if S[i] == "K":
        r = i

if (b1 + b2) % 2 != 0 and k1 < r < k2:
    print("Yes")
else:
    print("No")

