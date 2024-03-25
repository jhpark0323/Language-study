import sys

ipt = sys.stdin.readline
n = int(ipt().strip())
ls = list(map(int, ipt().strip().split()))

for i in ls:
    cnt = 0
    for j in ls:
        if i > j:
            cnt += 1
    print(cnt)