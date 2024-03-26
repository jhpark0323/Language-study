import sys

ipt = sys.stdin.readline
n = int(ipt().strip())
ls = list(map(int, ipt().strip().split()))

new_ls = list(set(ls))
new_ls.sort()
# print(new_ls)

new_dict = {}
for i in range(len(new_ls)):
    new_dict[new_ls[i]] = i

# print(new_dict)

for i in ls:
    print(new_dict[i], end = ' ')