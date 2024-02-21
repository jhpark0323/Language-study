# test_case 무조건 4개임?
for i in range(4):
    # 각각을 나눠 x y p q로 나타냄
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # print(x1, y1, p1, q1)
    # print(x2, y2, p2, q2)

    a = max(x1, x2)
    b = max(y1, y2)
    c = min(p1, p2)
    d = min(q1, q2)

    width = a - c
    height = b - d

    if width > 0 or height > 0:
        print('d')

    elif width == 0 and height == 0:
        print('c')

    elif width == 0 or height == 0:
        print('b')

    # a의 경우
    else:
        print('a')
