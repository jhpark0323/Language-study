import sys

def rotation(standard):
    start = arr[standard][standard]
    row = n-2*standard
    col = m-2*standard

    # 윗줄
    for i in range(col-1):
        arr[standard][standard+i] = arr[standard][standard+i+1]
    # 오른쪽
    for i in range(row-1):
        arr[standard+i][m-standard-1] = arr[standard+i+1][m-standard-1]
    # 아래쪽
    for i in range(col-1):
        arr[n-1-standard][m-1-standard-i] = arr[n-1-standard][m-1-standard-i-1]
    # 왼쪽
    for i in range(row-1):
        arr[n-1-standard-i][standard] = arr[n-1-standard-i-1][standard]

    # 기준점 저장해놓은 start로 바꿔주기
    arr[standard+1][standard] = start

ipt = sys.stdin.readline
n, m, r = map(int, ipt().strip().split())
# print(n, m, r)

arr = [list(map(int, ipt().strip().split())) for _ in range(n)]
# print(arr)

num = min(n, m) // 2

for _ in range(r):
    for standard in range(num):
        rotation(standard)

for i in arr:
    print(*i)