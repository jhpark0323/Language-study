import sys

arr = []
# 이렇게 쓸수도 있다고 함
# arr = [list(map(int, line.split())) for line in sys.stdin.read().splitlines() if line != '0 0 0']

while 1:
    line = sys.stdin.readline().strip()
    arr.append(list(map(int, line.split())))
    if arr[-1] == [0, 0, 0]:
        arr.pop()
        break

print(arr)

for i in arr:
    hypo = max(i)