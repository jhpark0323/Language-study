import sys

ipt = sys.stdin.readline
n, k = map(int, ipt().strip().split())
ls = [int(ipt().strip()) for _ in range(n)]
# print(ls)

cnt = 0
while 1:
    # 큰 돈부터 주기
    money = ls.pop()
    # 돈이 k보다 작으면
    if money <= k:
        # cnt에 k를 돈으로 나눈 몫을 더해줌
        cnt += k // money
        # k는 나머지로 재할당
        k %= money
        if k == 0:
            break

print(cnt)