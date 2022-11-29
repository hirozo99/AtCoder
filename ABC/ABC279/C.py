H, W = map(int, input().split())
s = [input() for _ in range(H)]
t = [input() for _ in range(H)]

arr_s = list(zip(*s))
arr_t = list(zip(*t))
arr_s.sort()
arr_t.sort()
if arr_s == arr_t:
    print("Yes")
else:
    print("No")
