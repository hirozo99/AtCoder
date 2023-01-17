N = int(input())

s_lst = []
t_lst = []

for i in range(N):
    s, t = map(str, input().split())
    s_lst.append(s)
    t_lst.append(t)
print(s_lst)
print(t_lst)

for i in range(N):
