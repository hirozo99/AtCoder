N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 合格者のリスト
ans=[]

# 数学の得点と受験番号リスト
mathp=[]

# i=0からi=N-1
for i in range(N):
    # 「数学の得点」,「受験番号のマイナス」を記録
    mathp.append([A[i], -(i+1)])
# 大きい順にソート
mathp.sort(reverse=True)

# リストの前からX人合格
# i=0からi=X-1
for i in range(X):
    # 答えに合格者の番号を格納
    ans.append(-mathp[i][1])
# 英語の点数と受験番号リスト
engp = []

# i=0からi=N-1
for i in range(N):
    if i+1 not in ans:
        engp.append([B[i], -(i+1)])
# 大きい順にソート
engp.sort(reverse=True)

# リストの前からY人合格
# i=0からi=Y-1
for i in range(Y):
    # 答えに合格者の番号を格納
    ans.append(-engp[i][1])

# 数学と英語の合計点数と受験番号リスト
mep = []

# i=0からi=N-1
for i in range(N):
    # 合格者のリストに番号がなければ
    if i+1 not in ans:
        mep.append([A[i]+B[i], -(i+1)])
# 大きい順にソート
mep.sort(reverse=True)

# リストの前からZ人合格
# i=0からi=-1
for i in range(Z):
    # 答えに合格者の番号を格納
    ans.append(-mep[i][1])

# 答えのリストをソート
ans.sort()

# x:ansの各要素
for x in ans:
    # xを出力
    print(x)


