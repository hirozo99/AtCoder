N = int(input())
S = input()

flag = False
for i in range(N):
    if S[i] == "o":
        flag = True
    elif S[i] == "x":
        print("No")
        exit()
    else:
        pass

if flag:
    print("Yes")
else:
    print("No")