def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        # memo[a][b][c] = w(20, 20, 20)
        return w(20, 20, 20)

    elif memo[a][b][c]:
        return memo[a][b][c]

    elif a < b and b < c:
        memo[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return memo[a][b][c]

    else:
        memo[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return memo[a][b][c]

memo = [[[0] * 21 for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, input().split())
    # 종료조건
    if a == b == c == -1:
        break

    # print(memo)

    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
