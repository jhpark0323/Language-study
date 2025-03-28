import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr = [input().strip() for _ in range(r)]

def check(num):
    ls = []
    for idx in range(c):
        newWord = ""
        for word in range(num, r):
            newWord += arr[word][idx]
        if newWord not in ls:
            ls.append(newWord)
        else:
            return False
    return True

left = 0
right = r-1

while (left <= right):
    mid = (left + right) // 2

    # 성공했으면 더 큰 숫자가 있는지 확인 해야함
    if check(mid):
        left = mid + 1
    # 실패 했으면 더 작은 범위에서 다시
    else:
        right = mid - 1

print(right)