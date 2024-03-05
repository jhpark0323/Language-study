import sys

# 입력 받을 수의 개수를 입력받습니다.
n = int(sys.stdin.readline())

# 입력된 수의 개수를 저장할 크기가 10,000인 배열을 선언합니다.
count = [0] * 10001

# 입력된 수를 하나씩 읽으면서 해당하는 인덱스의 count 배열 값을 1씩 증가시킵니다.
for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1

# count 배열을 순회하면서 각 인덱스의 값(count[i])이 0보다 큰 경우, 해당 인덱스를 출력합니다.
for i in range(10001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)
