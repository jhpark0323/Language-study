def back(start, count):
    if count == m:
        return print(*a)

    for i in range(start, n+1):
        a.append(i)
        back(i, count+1)
        a.pop()

n, m = map(int, input().split())
a = []
back(1, 0)