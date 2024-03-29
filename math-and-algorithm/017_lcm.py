#最大公約数を返す関数
def GCD(A, B):
    while A >= 1 and B >= 1:
        if A > B:
            A = A % B
        else:
            B = B % A
    if A >= 1:
        return A
    return B

#最小公倍数を返す関数
def LCM(A, B):
    return int(A / GCD(A, B)) * B

#入力
N = int(input())
A = list(map(int, input().split()))

#答えを求める
R = LCM(A[0], A[1])
for i in range(2, N):
    R = LCM(R, A[i])

#出力
print(R)
