#mathモジュールを用いた解答例
import math
print(math.factorial(int(input())))

#階乗の関数を作成した解答例
n = int(input())

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
print(fact(n))