x, y, z = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(y)] for _ in range(z)]
print(arr)

