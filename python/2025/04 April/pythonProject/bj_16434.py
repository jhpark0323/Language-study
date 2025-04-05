import sys
input = sys.stdin.readline

n, atk = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def check(target):
    my_atk = atk
    max_hp = target
    for i in range(n):
        if arr[i][0] == 1:
            a = arr[i][2] // my_atk # 몬스터가 a턴 후에 죽음
            b = arr[i][2] % my_atk
            c = target // arr[i][1] # 용사가 c턴 후에 죽음
            d = target % arr[i][1]

            if b != 0:
                a += 1
            if d != 0:
                c += 1

            if a > c:
                return False
            else:
                target -= (a-1) * arr[i][1]

        else:
            my_atk += arr[i][1]
            target += arr[i][2]
            if target > max_hp:
                target = max_hp

    return True

left = 0
right = sys.maxsize

while left <= right:
    mid = (left + right) // 2

    if check(mid):
        right = mid - 1
    else:
        left = mid + 1

print(left)
