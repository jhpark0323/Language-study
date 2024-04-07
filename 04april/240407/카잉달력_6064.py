T = int(input())

for _ in range(T):
    m, n, x, y = map(int, input().split())

    for i in range(m):
        for j in range(n):
            print(i+j)