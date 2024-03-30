n = int(input())

ls = [0] * 1001

# def f(n):
#     # ls[n]이 존재하면 바로 return
#     if ls[n]:
#         return ls[n]
#
#     if n == 1:
#         ls[1] = 1
#         return 1
#
#     if n == 2:
#         ls[2] = 3
#         return 3
#
#     ls[n] = f(n-1) + 2*f(n-2)
#     return ls[n]
#
# print(f(n))

ls[1] = 1
ls[2] = 3

for i in range(3, n+1):
    ls[i] = ls[i-1] + 2*ls[i-2]

print(ls[n] % 10007)