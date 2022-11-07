"""
N枚のカードがあり、左からi番目（1≤i≤N）のカードの色はAです。
A=1のとき赤色、A=2のとき黄色、A=3のとき青色です。同じ色のカードを2枚選ぶ方法は何通りありますか。
"""

#入力
N = int(input())
A = list(map(int, input().split()))

#赤・黄・青のカードの枚数をそれぞれ計算する
red = A.count(1)
yellow = A.count(2)
blue = A.count(3)
sum = red * (red - 1) // 2 + yellow * (yellow - 1) // 2 + blue * (blue - 1) // 2

#出力
print(sum)
