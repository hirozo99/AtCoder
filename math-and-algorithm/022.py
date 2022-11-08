"""
N 枚のカードがあり、左から i 番目のカードには整数 A が書かれています。
和が 100000 となる 2 枚のカードの選び方は何通りあるかを求めるプログラムを作成してください。
"""
# 入力
N = int(input())
A = list(map(int, input().split()))

# 答えを求める
cnt = [0 for i in range(100000)]
for i in range(N):
	cnt[A[i]] += 1

Answer = 0
for i in range(1, 50000):
	Answer += cnt[i] * cnt[100000 - i]
Answer += cnt[50000] * (cnt[50000] - 1) // 2

# 出力
print(Answer)
