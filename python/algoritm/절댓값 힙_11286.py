import heapq
import sys

# 최소 힙 생성
heap = []

n = int(input())
for _ in range(n):
    i = int(sys.stdin.readline())
    if i != 0:
        # 절댓값과 원래 값을 함께 힙에 추가
        heapq.heappush(heap, (abs(i), i))
    else:
        if not heap:
            print(0)
        else:
            # 원래 값을 출력
            print(heapq.heappop(heap)[1])
