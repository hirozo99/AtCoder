K = int(input())

h = 21 if K < 60 else 22
m = K % 60
print(f'{h}:{m:02}')