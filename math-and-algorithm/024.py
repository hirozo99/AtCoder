# 入力
N = int(input())
P = [None] * N
Q = [None] * N

for i in range(N):
	P[i], Q[i] = map(int, input().split())

# 答えの計算
ans = 0
for i in range(N):
	ans += Q[i] / P[i]

# 出力
print("%.7f" % ans)
