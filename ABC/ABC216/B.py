N = int(input())
S = ['']*N
T = ['']*N
for i in range(N):
    S[i],T[i] = map(str,input().split())
ans = 'No'
for i in range(N):
    for j in range(i+1,N):
        if S[i]==S[j] and T[i]==T[j]:
            ans = 'Yes'
print(ans)
