# 入力の受け取り
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())

# x1=x2の場合
if x1==x2:
    x4=x3
# x2=x3の場合
elif x2==x3:
    x4=x1
# x3=x1の場合
elif x3==x1:
    x4=x2

# y1=y2の場合
if y1==y2:
    y4=y3
# y2=y3の場合
elif y2==y3:
    y4=y1
# y3=y1の場合
elif y3==y1:
    y4=y2

# 答えの出力
print(x4,y4)

# 排他的論理和(X0R)を用いた実装例
ax, ay = 0, 0
for _ in range(3):
    x, y = map(int, input().split())
    ax ^= x
    ay ^= y
print(ax, ay)

