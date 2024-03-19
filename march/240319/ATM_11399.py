import sys

ipt = sys.stdin.readline
n = int(ipt().strip())
ls = list(map(int, ipt().strip().split()))
# print(ls)

ls.sort()
ans = 0
j = 0
for i in range(n, 0, -1):
    ans += ls[j] * i
    j += 1

print(ans)