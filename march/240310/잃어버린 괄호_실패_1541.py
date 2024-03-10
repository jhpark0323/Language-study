import copy

ls = input()

num = []

number = ''
for i in ls:
    # 숫자면
    if i.isdigit():
        # number에 하나씩 더하기
        number += i
    # 연산자면
    else:
        # number에 숫자가 들어있으면
        if number:
            # num에 append
            # str에 int까지 쓰는 이유는 0009이런것들에서 앞의 0을 지우기 위해
            # -> 나중에 eval할때 에러남
            num.append(str(int(number)))
            # 초기화
            number = ''
        # 연산자에 i append
        num.append(i)
# 마지막에 무조건 하나 남음
num.append(str(int(number)))

# 순서대로 숫자와 연산자가 하나씩 들어감
# print('num :', num)

n = len(num)

min_answer = float('inf')
for i in range(0, n, 2):
    for j in range(i+1, n+1, 2):
        new_num = copy.deepcopy(num)
        new_num.insert(i, '(')
        new_num.insert(j+1, ')')
        # print(new_num)
        answer = eval(''.join(new_num))
        # print(answer)
        if min_answer > answer:
            min_answer = answer

print(min_answer)