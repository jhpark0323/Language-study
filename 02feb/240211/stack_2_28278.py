n = int(input())

ls = [list(map(int, input().split())) for _ in range(n)]

# print(ls)

stack = []

for i in ls:
    # stack에 정수를 넣음
    if i[0] == 1:
        stack.append(i[1])

    # 스택이 비어있으면 pop으로 출력 없으면 -1 출력
    elif i[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)

    # 스택의 길이 출력
    elif i[0] == 3:
        print(len(stack))

    # 스택이 비어있는지 조사
    elif i[0] == 4:
        if stack:
            print(0)
        else:
            print(1)

    # 스택에 정수가 있으면 스택의 맨위를 출력
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)