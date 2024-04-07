import sys

def f(a, b):
    st = 0

    a_set = set(a)
    b_set = set(str(b))
    ba = a_set & b_set

    for ii in range(3):
        if a[ii] == b[ii]:
            st += 1
    # ball의 갯수는 교집합 갯수에서 strike 갯수 뺴기
    return st, len(ba)-st

input = sys.stdin.readline
n = int(input())
# arr = [list(map(int, input().strip().split())) for _ in range(n)]
arr = [list(input().strip().split()) for _ in range(n)]
# print(arr)

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        # 숫자가 다 달라야함
        if i == j:
            continue
        for k in range(1, 10):
            # 숫자가 다 달라야함
            if i == k or j == k:
                continue
            cnt = 0
            for ls in arr:
                a = str(100*i + 10*j + k)
                b = ls[0]
                strike, ball = f(a, b)
                real_strike, real_ball = int(ls[1]), int(ls[2])
                # 만약 진짜 st, ball과 구한게 같으면 cnt += 1
                if strike == real_strike and ball == real_ball:
                    cnt += 1
                # 하나라도 틀리면 다른 번호로 넘어감
                else:
                    break
            # 모든 조건을 만족해 cnt와 n이 같다면
            if cnt == n:
                ans += 1
                # print('a :',a)
                # print(strike, ball)
                # print(real_strike, real_ball)
print(ans)