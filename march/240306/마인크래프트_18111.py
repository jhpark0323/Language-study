import sys

# n : 세로, m : 가로, b : 시작시 가진 블럭의 수
n, m, b = map(int, sys.stdin.readline().strip().split())

arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
print(arr)

