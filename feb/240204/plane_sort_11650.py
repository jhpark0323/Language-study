n = int(input())

ls = [list(map(int, input().split())) for _ in range(n)]

ls.sort()

for i in range(n):
    print(*ls[i])