from math import ceil

x, y = map(int, input().split())

check = y - x

if check <= 0:
    print(0)
else:
    print(ceil((check / 10)))

# 他の実装例

# 入力の受け取り
X,Y=map(int,input().split())

# X<Yならば
if X<Y:
    # (Y-X)が10で割り切れる⇔(Y-X)÷10の余りが0　ならば
    if (Y-X)%10==0:
        # (Y-X)//10を出力
        print((Y-X)//10)
    # そうでないならば((Y-X)が10で割り切れない)
    else:
        # (Y-X)//10+1を出力
        print((Y-X)//10+1)
# そうでないならば(Y≤X)
else:
    # 0を出力
    print(0)