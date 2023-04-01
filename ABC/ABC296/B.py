masu = []

for i in range(8):
    masu.append(input())


for i in range(8):
    for j in range(8):
        if masu[i][j] == "*":
            a = chr(j+97)
            b = 8 - i

print(str(a)+str(b))