def f(num):
    ls = list(map(int, list(str(num))))
    return num + sum(ls)

n = int(input())

# print(f(n))

for i in range(1, n):
    if f(i) == n:
        print(i)
        break

else:
    print(0)