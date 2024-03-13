# def f(s, i):
#     global answer
#
#     if i == n:
#         if s == t:
#             answer = 1
#             print(answer)
#             exit()
#         return
#
#     elif s.count('A') > a:
#         return
#
#     elif s.count('B') > b:
#         return
#
#     f(s+'A', i+1)
#     f(s[::-1] + 'B', i+1)


s = input()
t = input()

# a = t.count('A')
# b = t.count('B')
# # print(t.count('A'))
# # print(t.count('B'))
#
# n = len(t)
#
# answer = 0
# f(s, len(s))
# print(answer)

answer = 0

while len(t) != len(s):
    # t의 맨뒤가 A이면
    if t[-1] == 'A':
        # t를 하나뺌
        t = t[:-1]

    elif t[-1] == 'B':
        t = t[:-1][::-1]

    else:
        if s == t:
            answer = 1
            break
    # S의 길이가 t의 길이보다 항상 작으므로 시작하자마자 둘이 같을 수는 없음
    if t == s:
        answer = 1
        break
print(answer)