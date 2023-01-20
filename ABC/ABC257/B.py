N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

# N+1マスのマス目を用意
# 0ならばコマがない
# 1ならばコマがある
box = [0 for _ in range(N+1)]
for i in range(K):
    box[A[i]] = 1

# 左からx番目のコマが置かれたマス目を返す関数
def koma_num(x):
    count = 0
    for i, now_koma in enumerate(box):
        if now_koma == 1:
            count += 1
            if count == x:
                return int(i)
                break


for i in range(Q):
    k = koma_num(L[i])
    if not koma_num(L[i]) == len(box)-1:
        if box[k+1] == 1:
            pass
        else:
            box[k] = 0
            box[k+1] = 1
    else:
        pass

ans = []
for i in range(len(box)):
    if box[i] == 1:
        ans.append(i)

print(*ans)

# 解説の実装例
# n,k,q = map(int, input().split())
# a = list(map(int,input().split()))
# l= list(map(int,input().split()))
#
# for i in range(q):
#     if(a[l[i]-1] == n):
#         continue
#     elif(l[i]==k):
#         a[l[i]-1]+=1
#     elif(a[l[i]-1]+1<a[l[i]]):
#         a[l[i]-1]+=1
#
# print(*a)
