def f(i, k, s):
    global min_v
    global cnt
    cnt += 1
    if i == k:
        # print(*p)
        if min_v > s:
            min_v = s
        # print(s)
    # 뒤로 더 안가도 이미 선택한 원소의 합 s가 최솟값보다 크면 걍 종료
    elif s >= min_v:
        return
    else:
        # p[i]자리에 올 원소 p[j]를 결정
        for j in range(i, k):
            # p[i] <-> p[j]
            p[i], p[j] = p[j], p[i]
            f(i+1, k, s+arr[i][p[i]])
            # p[i] <-> p[j] (원상복구)
            p[i], p[j] = p[j], p[i]

T = int(input())

for test_case in range(1, T+1):

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    p = [i for i in range(n)]
    cnt = 0
    min_v = 100
    f(0, n, 0)
    print(min_v, cnt)