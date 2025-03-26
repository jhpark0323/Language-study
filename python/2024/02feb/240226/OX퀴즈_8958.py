T = int(input())

for tc in range(T):
    test_case = list(input())

    ls = [0] * len(test_case)

    # # ls에 O가 있는부분 1로 채우기
    # for i in range(len(test_case)):
    #     if test_case[i] == 'O':
    #         ls[i] = 1
    # print(ls)

    for i in range(len(test_case)):
        # 처음엔 확인 해봄
        if i == 0:
            if test_case[i] == 'O':
                ls[i] = 1

        else:
            if test_case[i] == 'O':
                ls[i] = ls[i-1]+1

    print(sum(ls))