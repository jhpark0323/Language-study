while 1:
    sentence = input()
    # input값이 .이면 break
    if sentence == '.':
        break

    stack = []
    # 맞다를 기준으로 함
    answer = 'yes'

    for i in sentence:
        if i in '([':
            stack.append(i)

        # 닫히는 소괄호 일때
        elif i == ')':
            # stack이 비어있지 않고 stack의 마지막원소가 열리는 소괄호 일때
            if stack and stack[-1] == '(':
                stack.pop()
                continue
            # 아니면 answer = 'no'
            else:
                answer = 'no'
                break

        # 닫히는 대괄호 일때
        elif i == ']':
            # stack이 비어있지 않고 stack의 마지막원소가 열리는 대괄호 일때
            if stack and stack[-1] == '[':
                stack.pop()
                continue
            # 아니면 answer = 'no'
            else:
                answer = 'no'
                break
    # 만약 stack이 차있으면 탈락
    if stack:
        answer = 'no'
    print(answer)