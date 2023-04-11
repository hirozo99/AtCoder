H, W = map(int, input().split())
S = [list(input()) for i in range(H)]

flag = True
for i in range(H):
    for j in range(W-1):
        if flag:
            if S[i][j] == "T":
                if S[i][j+1] == "T":
                    S[i][j] = "P"
                    S[i][j+1] = "C"



for i in range(H):
    print("".join(S[i]))