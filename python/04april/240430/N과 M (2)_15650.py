# def back(count):
#     if count == m:
#         return print(*a)
#
#     for i in range(1, n+1):
#         if not a or i > a[-1]:
#             a.append(i)
#             back(count+1)
#             a.pop()
#
# n, m = map(int, input().split())
# a = []
# back(0)

# 이게 좀 더 나을듯
def back(start, count):
    if count == m:
        return print(*a)

    for i in range(start, n+1):
        if i not in a:
            a.append(i)
            back(i+1, count+1)
            a.pop()

n, m = map(int, input().split())
a = []
back(1, 0)