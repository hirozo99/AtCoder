# 計算量がO(v)の実装例
v, a, b, c = map(int, input().split())

while True:
    if v < a:
        print("F")
        exit()
    v -= a
    if v < b:
        print("M")
        exit()
    v -= b
    if v < c:
        print("T")
        exit()
    v -= c

# 計算量がO(1)の実装例
v, a, b, c = map(int, input().split())

v %= a + b + c
if v < a:
    print("F")
elif v < a + b:
    print("M")
else:
    print("T")
