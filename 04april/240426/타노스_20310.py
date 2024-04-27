ls = list(input())
# print(ls)

zero_count = ls.count('0')
one_count = ls.count('1')
# print(zero_count, one_count)

zero_count //= 2
one_count //= 2

for _ in range(one_count):
    ls.remove('1')

ls = ls[::-1]

for _ in range(zero_count):
    ls.remove('0')

print(''.join(ls[::-1]))