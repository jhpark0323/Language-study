def f(i, k, arr):
    global min_v
    global cnt
    cnt += 1
    if i == k:
        # print(*p)

        # 선택한 원소의 합
        s = 0
        # j행에 대해
        for j in range(k):
            # j행에서 p[j]열을 고른 경우의 합 구하기
            s += arr[j][p[j]]
        if min_v > s:
            min_v = s
        # print(s)

    else:
        # p[i]자리에 올 원소 p[j]를 결정
        for j in range(i, k):
            # p[i] <-> p[j]
            p[i], p[j] = p[j], p[i]
            f(i+1, k, arr)
            # p[i] <-> p[j] (원상복구)
            p[i], p[j] = p[j], p[i]

T = int(input())

for test_case in range(1, T+1):

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    p = [i for i in range(n)]
    cnt = 0
    min_v = 100
    f(0, n, arr)
    print(min_v, cnt)