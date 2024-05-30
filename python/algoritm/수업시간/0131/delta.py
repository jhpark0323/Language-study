# 순서대로 우, 하, 좌, 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

n = 5
arr = [[i for i in range(n)] for _ in range(n)]
print(arr)

# 우, 하, 좌, 상 순으로 순회
for i in range(n):
    for j in range(n):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if (0 <= ni < n) & (0 <= nj < n):
                print(arr[ni][nj], end=' ')
        print()


i = 3
j = 4
for k in range(4):
    ni = i + di[k]
    nj = j + dj[k]
    print(ni, nj)
'''
3 5
4 4
3 3
2 4
'''