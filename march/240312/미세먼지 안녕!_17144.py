from pprint import pprint

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
# pprint(arr)

# t초가 지난 후를 구하기 위해 t초간 순회
for time in range(t):
    # 1. 미세먼지 확산
    for i in range(r):
        for j in range(c):
            # -1과 0이 아니면
            if arr[i][j] and arr[i][j] != -1:
