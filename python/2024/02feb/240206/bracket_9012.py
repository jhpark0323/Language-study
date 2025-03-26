T = int(input())

ls = [input() for _ in range(T)]

for bracket_ls in ls:
    stack = []
    answer = 'YES'
    # print(bracket_ls)

    for i in bracket_ls:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                answer = 'NO'
                break
    if len(stack) != 0:
        answer = 'NO'

    print(answer)