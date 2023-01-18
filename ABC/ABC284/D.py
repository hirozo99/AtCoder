# pypyで提出

# 平方根計算用にsqrtをインポート
from math import sqrt

# 入力の受け取り
T=int(input())

# T回
for i in range(T):
    # 入力の受け取り
    N=int(input())

    # x=2~10^7
    for x in range(2,10**7+1):
        # Nがx^2で割り切れる場合
        # ⇔p=x
        if N%x**2==0:
            # q=N//x^2
            print(x,N//x**2)
            # 次のNへ
            break
        # Nがxで割り切れる場合
        # ⇔q=x
        elif N%x==0:
            # p=√(N//q)
            print(int(sqrt(N//x)),x)
            # 次のpへ
            break
