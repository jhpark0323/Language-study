from itertools import combinations

def f(a, b):
    cnt = 0
    for i in range(4):
        # 둘의 글자를 비교 했을 때 다르면 1씩 증가
        if a[i] != b[i]:
            cnt += 1
    return cnt

T = int(input())

for _ in range(T):
    n = int(input())
    ls = list(input().split())
    # print(ls)

    if n >= 33:
        print(0)
        continue

    combi = list(combinations(ls, 3))
    # print(combi)

    min_cnt = float('inf')
    for group in combi:
        first, second, third = group[0], group[1], group[2]
        cnt1 = f(first, second)
        cnt2 = f(second, third)
        cnt3 = f(third, first)

        ans = cnt1 + cnt2 + cnt3

        if min_cnt > ans:
            min_cnt = ans

        # 0이면 더 볼필요 없잖아?
        if min_cnt == 0:
            break

    print(min_cnt)