n = int(input())

long_times = n // 4 + 1

if n % 4 == 0:
    long_times = n // 4
else:
    long_times = n // 4 + 1

print('long ' * long_times + 'int')