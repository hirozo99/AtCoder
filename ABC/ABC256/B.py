# 入力の受け取り
N=int(input())
A=list(map(int,input().split()))

# Pに初期値0を入れる
P=0

# 駒があるマス目
# 最初はマス0に1個
Koma=[0]

# i=0~(N-1)
for i in range(N):
    # 新しい駒の場所
    NewKoma=[0]

    # Komaの値を順にxへ入力して処理
    for x in Koma:
        # (x+A[i])<4⇔マス目の範囲内なら
        if x+A[i]<4:
            # 新しいマス目を記録
            NewKoma.append(x+A[i])
        # そうでないなら(マス目の範囲を超えたら)
        else:
            # Pにプラス1
            P+=1

    # KomaをNewKomaで更新
    Koma=NewKoma

# 答えの出力
print(P)