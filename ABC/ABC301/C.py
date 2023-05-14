S = input()
T = input()

at_list = ["a", "t", "c", "o", "d", "e", "r"]
S = S.replace('@', '')
T = T.replace('@', '')


print(sorted(S))
print(sorted(T))

and_list = set(S) | set(T)
print(and_list)

if and_list in at_list:
    print("Yes")
else:
    print("No")
