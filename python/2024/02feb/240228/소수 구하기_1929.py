import math

m, n = map(int, input().split())

def find(num):
    if num == 1:
        return

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return
    else:
        return num


for i in range(m, n+1):
    if find(i):
        print(i)

# int((num) ** (1/2))