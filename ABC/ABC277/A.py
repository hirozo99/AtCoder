#入力
N, X = map(int, input().split())
P = list(map(int, input().split()))

#答えを求める
for i in range(N):
    if P[i] == X:
        print(i+1)