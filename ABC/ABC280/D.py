import sys
import math
input = sys.stdin.readline
K = int(input())

def prime_factorize(K):
    a = []
    while K % 2 == 0:
        a.append(2)
        K //= 2
    f = 3
    while f * f <= K:
        if K % f == 0:
            a.append(f)
            K //= f
        else:
            f += 2
    if K != 1:
        a.append(K)
    return a

if len(prime_factorize(K)) == 1:
    print(*prime_factorize(K))
else:
    print(max(prime_factorize(K)))
# print(math.factorial())