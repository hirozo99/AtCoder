N = int(input())

a = 0
b = 0
for i in range(N):
    S = input()
    if S == "For":
        a += 1
    else:
        b += 1

if a > b:
    print("Yes")
else:
    print("No")
