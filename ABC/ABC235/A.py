abc = list(input())

a = abc[0]
b = abc[1]
c = abc[2]

def num(x, y, z):
    xyz = int(x) * 100 + int(y) * 10 + int(z)
    return xyz
print(num(a, b, c) + num(b, c, a) + num(c, a, b))

# 解説の実装例
a, b, c = input()
abc = a + b + c
bca = b + c + a
cab = c + a + b
ans = int(abc) + int(bca) + int(cab)
print(ans)
