import sys

ipt = sys.stdin.readline

n, m = map(int, ipt().strip().split())

pw_dict = {}
for i in range(n):
    site, pw = ipt().strip().split()
    pw_dict[site] = pw

for i in range(m):
    site = ipt().strip()
    print(pw_dict[site])