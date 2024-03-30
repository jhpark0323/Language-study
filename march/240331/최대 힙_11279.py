import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())
hq = []
for i in range(n):
    ipt = int(input().strip())

    if ipt == 0:
        if hq:
            print(-heappop(hq))
        else:
            print(0)

    else:
        heappush(hq, -ipt)