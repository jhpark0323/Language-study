a, b, c, d, e, f = map(int, input().split())

# y = (c - a * x) / b
# dx + e(c-ax)/b = f
# dx + ec/b - eax/b = f
# (d-ea/b)x = f - ec/b

# x = (f - e*c/b) / (d-e*a/b)
# y = (c - a * x) / b
#
# print(int(x), int(y))

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            exit(print(x, y))