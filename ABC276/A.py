s = str(input())

s_list = list(s)
ans = []
for i in range(len(s_list)):
    if s_list[i] == "a":
        ans.append(i+1)

if ans:
    print(ans[-1])
else:
    print(-1)