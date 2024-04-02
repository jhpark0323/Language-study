import sys

def binary_search(num):
    start = 0
    end = n-1

    # 찾는 수와 mid가 같아질 때 까지
    while start <= end:
        mid = (start + end) // 2

        if ls_have[mid] == num:
            return mid

        elif ls_have[mid] < num:
            start = mid + 1

        else:
            end = mid - 1
    return -1


n = int(sys.stdin.readline().strip())
ls_have = list(map(int, sys.stdin.readline().strip().split()))

m = int(sys.stdin.readline().strip())
ls_count = list(map(int, sys.stdin.readline().strip().split()))

# print(n)
# print(ls_have)
# print(m)
# print(ls_count)

ls_have.sort()

for i in ls_count:

    # 찾은 숫자가 있는 idx
    idx = binary_search(i)

    # idx가 값이 있으면
    if idx != -1:
        cnt = 1
    # 없으면
    else:
        cnt = 0
    # 그 주위에 더 있을 수도 있음
    # idx보다 큰 부분 찾기
    j = 1
    # 범위안에 있고 i와 같으면
    while 0 <= idx+j < n and ls_have[idx+j] == i:
        cnt += 1
        j += 1

    k = 1
    while 0 <= idx-k < n and ls_have[idx-k] == i:
        cnt += 1
        k += 1

    print(cnt, end=' ')