n = int(input())

def f(n):
    ls = [0] * 16
    ls[0] = 4

    for i in range(1, n+1):
        ls[i] = (ls[i-1] ** (1/2) + ls[i-1] ** (1/2) - 1) ** 2

    return int(ls[n])

print(f(n))