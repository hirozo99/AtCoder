#整数Nが与えられます。 Nの約数を列挙してください。
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

n = int(input())
print(*make_divisors(n))
