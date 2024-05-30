T = int(input())

for _ in range(T):
    m, n, x, y = map(int, input().split())

    # mk + x = nk' + y 를 만족하는 정수 해 k, k'가 존재하면 가능
    # mk = nk' + y - x
    # k'는 0부터 k'까지
    ans = -1
    for i in range(n+1):
        if (n*i + y - x) % m == 0:
            ans = n*i + y
            break
    print(ans)