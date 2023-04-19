S_list = []
ans_list = ["H", "2B", "3B", "HR"]

for i in range(4):
    S = input()
    S_list.append(S)

if set(S_list) == set(ans_list) :
    print("Yes")
else:
    print("No")