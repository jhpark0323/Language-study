'''
치킨 식권 세장 -> 피자 식권 1장
피자 식권 3장 -> 햄버거 식권 1장
햄버거 식권 3장 -> 치킨 식권 1장
'''

# a : 치킨, b : 피자, c : 햄버거 명수
a, b, c = map(int, input().split())
# 치킨 피자 햄버거 식권
x, y, z = map(int, input().split())

s = a+b+c

for _ in range(3):
    if a > 0:
        a -= x
        x = 0
    if b > 0:
        b -= y
        y = 0
    if c > 0:
        c -= z
        z = 0
    # a, b, c에는 아직 식권을 못받은 인원이 담겨있다
    # 단 음수나 0이면 그 수의 절댓값 만큼 식권이 남음
    # 남은 식권으로 다른 식권 만들기

    if a <= 0:
        if a == 0:
            pass
        else:
            x = abs(a)
            # x는 끝났으니 가능한 전부 y로 넘겨줌
            a = 0
            # a가 0이나 음수이면 남은 갯수의 절댓값은 식권임
            y += x // 3
            x %= 3

    if b <= 0:
        if b == 0:
            pass
        else:
            y = abs(b)
            # y는 끝났으니 가능한 전부 z로 넘겨줌
            b = 0
            # b가 0이나 음수이면 남은 갯수의 절댓값은 식권임
            z += y // 3
            y %= 3

    if c <= 0:
        if c == 0:
            pass
        else:
            z = abs(c)
            # z는 끝났으니 가능한 전부 x로 넘겨줌
            c = 0
            # c가 0이나 음수이면 남은 갯수의 절댓값은 식권임
            x += z // 3
            z %= 3


print(s-a-b-c)