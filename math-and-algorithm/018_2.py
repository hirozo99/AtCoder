#コンビニには N 個の品物が売られており、i番目（1≤i≤N）の商品の値段はA円です。異なる2つの品物を買う方法のうち、合計金額が500円となるものは何通りありますか。

N = input()
A = list(map(int, input().split()))
ans = 0
ans += A.count(100) * A.count(400)
ans += A.count(200) * A.count(300)
print(ans)
