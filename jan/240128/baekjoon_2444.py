n = int(input())

for i in range(n):
    print(' ' * (n-i-1) + '*' * (2*i +1))

for i in range(n-1):
    print(' ' * (i+1) + '*' * (2*n - 3 - 2*i))
