N = int(input())
X = list(map(int, input().split()))

X.sort()
for i in range(N):
    X.pop(0)
    X.pop(-1)


cnt = 0
for i in X:
    cnt += i

ans = cnt / len(X)
print(f'{ans:.15f}')

"""
# 短い実装方法
N = int(input())
X = list(map(int, input().split()))
X.sort()

x = X[N:-N]

# print(x)
print(sum(x)/(3*N))
"""