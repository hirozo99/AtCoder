N = int(input())
W = list(map(str, input().split()))

kw = ["and", "not", "that", "the", "you"]
ans = 0
for i in W:
    if i in kw:
        ans += 1
    else:
        pass
if ans:
    print("Yes")
else:
    print("No")
