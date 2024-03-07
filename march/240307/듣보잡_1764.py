# n : 듣도, m : 보도
n, m = map(int, input().split())

set_n = set(input() for _ in range(n))
set_m = set(input() for _ in range(m))

ls = list(set_m & set_n)
# print(ls)

print(len(ls))
ls.sort()
for i in ls:
    print(i)