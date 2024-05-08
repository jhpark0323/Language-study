n = int(input())
word = input()

stack = []
max_bear = 0
bear = 0
for i in range(n):
    new_word = word[i]

    # stack에 값이 들어 있을 경우
    if stack:
        # 전에 들어있던거
        pre_word = stack[-1]
        # 전에 들었던거랑 지금꺼랑 다르면
        if pre_word != new_word:
            # 빼기
            stack.pop()
            bear -= 1

        # 같으면
        else:
            stack.append(new_word)
            bear += 1
            if bear > max_bear:
                bear = max_bear
            print('같으면', bear)
            print('같으면', max_bear)

    # stack이 비어있으면
    else:
        stack.append(new_word)
        bear += 1
        if bear > max_bear:
            max_bear = bear
        print(bear)
        print(max_bear)
    #
    # print(stack)

# 다 끝났을 때 stack이 비어있지 않으면 만들 수 없는 문자열임
if stack:
    print(-1)

else:
    print(max_bear)