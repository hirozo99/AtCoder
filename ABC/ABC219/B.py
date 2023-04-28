s_list = []

for i in range(3):
    S = input()
    s_list.append(S)
T = input()

ans = ""
for i in range(len(T)):
    ans += s_list[int(T[i])-1]

print(ans)