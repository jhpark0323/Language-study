ipt = input()

stack = []
cnt = 0
ans = 0
for i in ipt:
    # 여는 괄호 이면
    if i == '(':
        stack.append(i)
        # 쇠막대기의 갯수를 하나 늘림
        cnt += 1
    # 닫는 괄호이면
    else:
        # 쇠막대기의 갯수를 하나 줄인다
        cnt -= 1
        # 하나 빼기
        stack.pop()
        # 앞에가 여는 괄호이면 닫히는 괄호가 레이저 였다는 뜻
        if pre_ == '(':
            # ans에 쇠막대기의 갯수만큼 더해준다
            ans += cnt

        # 앞에가 닫는 괄호였으면 쇠막대기의 끝이라는 뜻
        else:
            # 쇠막대기가 끝났으므로 레이저에 의해 안잘려도 남은 한개 더해줘야함
            ans += 1

    # 이번게 뭔지 적어 놓기
    pre_ = i

print(ans)