import sys

T = int(input())

for _ in range(T):
    m, n, x, y = map(int, sys.stdin.readline().split())

    # mk + x = nk' + y 를 만족하는 정수 해 k, k'가 존재하면 가능
    # mk = nk' + y - x
    # mk + x - y = nk'
    # k'는 0부터 k'까지
    ans_1 = -1
    ans_2 = -1
    for i in range(n+1):
        if (n*i + y - x) % m == 0:
            ans_1 = n*i + y
            break

    for i in range(m+1):
        if (m*i + x - y) % n == 0:
            ans_2 = m*i + x
            # print(m, i, x)
            break
    # print(ans_2)
    ans = max(ans_1, ans_2)
    print(ans)
    # print(ans_1, ans_2)