n = 5
arr = [[i for i in range(n)] for _ in range(n)]
print(arr)

# 우, 하, 좌, 상 순으로 순회
for i in range(n):
    for j in range(n):
        for di, dj in [[0,1], [1,0], [0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if (0 <= ni < n) & (0 <= nj < n):
                print(arr[ni][nj], end = ' ')
        print()