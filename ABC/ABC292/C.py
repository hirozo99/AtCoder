N = int(input())

def count_combinations(n):
    count = 0
    for a in range(1, n+1):
        for b in range(1, n//a+1):
            for c in range(1, n+1):
                d = (n - a*b)//c
                if d >= 1 and a*b + c*d == n:
                    count += 1
    return count

print(count_combinations(N))