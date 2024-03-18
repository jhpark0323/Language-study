import math

'''
코시슈바르츠
(a**2 + b**2)(x**2 + y**2) >= (x+y)**2
-> (x**2 + y**2) >= (x+y)**2 / (a**2 + b**2)
'''

n, m = map(int, input().split())
s = input()
t = input()

ls_0 = []
ls_1 = []
for i in range(n+m):
    if s[i] == t[i]:
        pass
    else:
        if s[i] == '0':
            ls_0.append(i)

        else:
            ls_1.append(i)
# print(ls_0)
# print(ls_1)

num = 0
while ls_0:
    num += abs(ls_0.pop()-ls_1.pop())

ans = num**2 / 2

print(math.ceil(ans))