s = [list(input()) for _ in range(10)]

a = []
b = []
for i in range(10):
    for j in range(10):
        if s[i][j] == "#":
            a.append(i)
            b.append(j)
a = set(a)
b = set(b)
print(min(a)+1, max(a)+1)
print(min(b)+1, max(b)+1)

#AC