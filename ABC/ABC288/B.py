N, K = map(int, input().split())

S_list = []
for i in range(N):
    S = input()
    S_list.append(S)

S_list = S_list[:K]
S_list.sort()
for i in range(K):
    print(S_list[i])
