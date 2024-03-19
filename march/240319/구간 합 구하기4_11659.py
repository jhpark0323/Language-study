import sys
ipt = sys.stdin.readline

n, m = map(int, ipt().strip().split())
ls = list(map(int, ipt().strip().split()))
arr = [list(map(int, ipt().strip().split())) for _ in range(m)]
# print(ls)
# print(arr)

new_ls = [0]*(n+1)
for i in range(n+1):
    if i == 0:
        continue
    if i == 1:
        new_ls[i] = ls[0]
    else:
        new_ls[i] = new_ls[i-1] + ls[i-1]
# print(new_ls)

for i in arr:
    ans = new_ls[i[1]] - new_ls[i[0]-1]
    print(ans)