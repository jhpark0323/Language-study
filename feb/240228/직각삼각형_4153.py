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

# print(arr)

for i in arr:
    # 제일 큰게 빗변
    hypo = i.pop(i.index(max(i)))
    # 남은 두개가 남은 변들
    a, b = i[0], i[1]

    if a ** 2 + b ** 2 == hypo ** 2:
        answer = 'right'

    else:
        answer = 'wrong'

    print(answer)