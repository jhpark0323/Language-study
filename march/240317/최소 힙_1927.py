import sys
import heapq

ipt = sys.stdin.readline

n = int(ipt().strip())

heap = []
heapq.heapify(heap)
for i in range(n):
    new = int(ipt().strip())

    if new == 0:
        # 비어있으면
        if not heap:
            print(0)
        # 있으면
        else:
            print(heapq.heappop(heap))

    else:
        heapq.heappush(heap, new)

