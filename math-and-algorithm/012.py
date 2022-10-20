def isprime(N):
    if N < 2:
        return "No"
    for i in range(2, int(N ** 0.5)): #ルートN以下まで計算しないと時間超過となってしまう
        if N % i == 0:
            return "No"
    return "Yes"

N = int(input())
print(isprime(N))
