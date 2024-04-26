ls = sorted(list(input()))
# print(ls)

zero_count = ls.count('0')
one_count = ls.count('1')
# print(zero_count, one_count)

zero_count //= 2
one_count //= 2

if zero_count == 0:
    exit(print(''.join(ls[zero_count:])))

elif one_count == 0:
    exit(print(''.join(ls[zero_count:])))

print(''.join(ls[zero_count:-one_count]))