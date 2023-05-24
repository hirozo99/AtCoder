K = int(input())
A, B = input().split()

def cal(x):
    decimal = 0
    for i in range(len(x)-1, -1, -1):
        decimal += int(x[i]) * (K**abs(i+1-len(x)))
    return decimal
print(cal(A)*cal(B))