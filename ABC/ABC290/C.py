from itertools import combinations
N, K = map(int, input().split())
A = list(map(int, input().split()))

def mex(nums):
    smallest = 0
    nums_set = set(nums)

    while True:
        if smallest not in nums_set:
            return smallest
        smallest += 1

def subsequence(a, k):
    subsequences = []
    for comb in combinations(a, k):
        subsequences.append(list(comb))
    return subsequences

check = subsequence(A, K)
ans = 0

for i in range(len(check)):
    if max(mex(check[i]), ans) != ans:
        ans = max(mex(check[i]), ans)
print(ans)