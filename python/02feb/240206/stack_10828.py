n = int(input())

ls = [list(input().split()) for _ in range(n)]

# print(ls)

stack = []
for i in ls:
    if i[0] == 'push':
        # push면 i[1]을 int로 stack에 append
        stack.append(int(i[1]))
    elif i[0] == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif i[0] == 'size':
        print(len(stack))
    elif i[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
