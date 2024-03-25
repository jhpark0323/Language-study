import sys
from pprint import pprint

ipt = sys.stdin.readline

# delta
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

n, m, k = map(int, ipt().strip().split())
arr = [list(map(int, list(ipt().strip()))) for _ in range(n)]
pprint(arr)

