T = int(input())

for _ in range(T):
    pw = input()
    left = []
    right = []
    for i in pw:
        if i == '>':
            # 오른쪽에 있는걸 왼쪽에다 붙이기
            if right:
                left.append(right.pop())

        elif i == '<':
            # 왼쪽에 있는걸 오른쪽에 붙이기
            if left:
                right.append(left.pop())

        elif i == '-':
            # left 비어있지 않다면
            if left:
                left.pop()

        else:
            left.append(i)

    print(''.join(left) + ''.join(reversed(right)))