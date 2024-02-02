n, b = map(int, input().split())

# print(chr(65))  # A

b_jinbub = ''

while n != 0:
    mod = n % b
    if mod >= 10:
        mod = chr(mod + 55)
    else:
        mod = str(mod)
    b_jinbub += mod

    n //= b

print(b_jinbub[::-1])