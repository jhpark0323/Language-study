def back(count):
    if count == m:
        return print(*a)

    for i in range(1, n+1):
        a.append(i)
        back(count+1)
        a.pop()

n, m = map(int, input().split())
a = []
back(0)