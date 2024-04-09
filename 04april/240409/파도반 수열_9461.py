T = int(input())

for _ in range(T):
    n = int(input())
    if n == 1 or n == 2 or n == 3:
        print(1)
        continue
    elif n == 4 or n == 5:
        print(2)
        continue

    ls = [0] * (n+1)
    ls[1] = 1
    ls[2] = 1
    ls[3] = 1
    ls[4] = 2
    ls[5] = 2
    for i in range(6, n+1):
        ls[i] = ls[i-1] + ls[i-5]

    print(ls[n])