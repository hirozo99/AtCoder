N, K = map(int, input().split())
A = list(map(int, input().split()))

a = list(set(A))
# print(a)
a.sort()
c = 0
for i in a:
    if c == i:
        c += 1
    else:
        break
# print(c)
print(min(K, c))