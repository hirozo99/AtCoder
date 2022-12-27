N, Q = map(int, input().split())

lst = []
ans = []
for n in range(N):
    l = list(map(int, input().split()))
    lst.append(l[1:])
# print(lst)

for q in range(Q):
    s, t = list(map(int, input().split()))
    ans.append(lst[s-1][t-1])

for i in range(len(ans)):
    print(ans[i])

#AC