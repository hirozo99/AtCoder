# N の約数の個数をカウント
def divisors(N):
    num=0
    for i in range(1,N+1):
        if i*i>N:
            break
        if N%i!=0:
            continue

        num+=1
        if N//i!=i:
            num+=1

    return num