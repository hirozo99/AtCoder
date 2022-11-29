import sys
input = sys.stdin.readline
X, Y, N = map(int, input().split())

ans = min(N * X, (N // 3) * Y + (N % 3) * X)
print(ans)

