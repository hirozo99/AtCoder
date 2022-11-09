#入力
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#答えを求める
ans = 0
for i in range(N):
	ans += (1 / 3) * A[i] + (2 / 3) * B[i]

#出力
print("%.7f" % ans)
