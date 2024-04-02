n = int(input())

ls = [list(map(int, input().split())) for _ in range(n)]

# print(ls)

stack = []
cnt = 0
for i in ls:
    if i[0] == 1:
        stack.append(i[1])
        cnt += 1

    elif i[0] == 2:
        if cnt > 0:
            print(stack.pop())
            cnt -= 1
        else:
            print(-1)

    elif i[0] == 3:
        print(cnt)

    elif i[0] == 4:
        if cnt > 0:
            print(0)
        else:
            print(1)

    else:
        if cnt > 0:
            print(stack[-1])
        else:
            print(-1)