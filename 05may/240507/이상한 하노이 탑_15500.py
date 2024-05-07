n = int(input())
ls_1 = list(map(int, input().split()))
ls_2 = []
ls_3 = []

ans_ls = []
while True:
    # ls_1에 n이 있다면
    if n in ls_1:
        # 현재 쓸 거 pop
        now = ls_1.pop()
        # 현재 pop한것이 n이면
        if now == n:
            ls_3.append(now)
            ans_ls.append([1, 3])
            # n 한개씩 줄이기
            n -= 1
        # n이 아니면
        else:
            # 2에다가 담기
            ls_2.append(now)
            ans_ls.append([1, 2])

    elif n in ls_2:
        # 현재 쓸거 pop
        now = ls_2.pop()
        # 현재 pop한것이 n이면
        if now == n:
            ls_3.append(now)
            ans_ls.append([2, 3])
            # n 한개씩 줄이기
            n -= 1
        # n이 아니면
        else:
            # 1에다가 담기
            ls_1.append(now)
            ans_ls.append([2, 1])


    if n == 0:
        break

print(len(ans_ls))
for i in ans_ls:
    print(*i)