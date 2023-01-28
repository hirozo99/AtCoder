N, M = map(int, input().split())

s_list =[]
t_list = []
for i in range(N):
    s_list.append(input())

for i in range(M):
    t_list.append(input())

check = list(set(t_list))

count = 0
for i in range(N):
    for j in range(len(check)):
        if s_list[i][3:] == check[j]:
            count += 1

print(count)