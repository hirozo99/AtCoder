N = int(input())
S = list(map(int, input().split()))

ans_list = []
ans_list.append(S[0])
for i in range(1, N):
    ans_list.append(S[i] - S[i-1])
print(*ans_list)