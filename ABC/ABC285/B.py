N = int(input())
S = "$" + input()

for i in range(1, N):
    cnt = 0
    for j in range(1, N+1-i):
        if S[j] == S[j+i]:
            break
        else:
            cnt += 1
    print(cnt)
