#自然数Nを素因数分解するプログラムを作成してください。

# 素因数分解
def prime_factorization(N):
	Answer = []
	LIMIT = int(N ** 0.5)
	for i in range(2, LIMIT + 1):
		while N % i == 0:
			N /= i
			Answer.append(i)

	if N >= 2:
		Answer.append(int(N))

	print(*Answer)

N = int(input())

# 出力
prime_factorization(N)
