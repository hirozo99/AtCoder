N, K = map(int, input().split())

X = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lst = []
for i in range(len(X)):
    lst.append(X[i] * N)
ans_str = "".join(lst)
print(ans_str[K-1])

#解説の実装例
n, x = map(int, input().split())
print(chr(ord("A") + (x-1)//n))