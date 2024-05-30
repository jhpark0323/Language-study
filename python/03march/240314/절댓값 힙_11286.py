import heapq
import sys

# 최소 힙 생성
heap_over = []
heap_under = []

n = int(input())
# 원소 추가
for _ in range(n):
    i = int(sys.stdin.readline())

    if i > 0:
        heapq.heappush(heap_over, i)

    # 음수는 -를 포함해서 넣음 -> heapq는 최솟값만 뽑아서
    elif i < 0:
        heapq.heappush(heap_under, -i)

    else:
        if not heap_over and not heap_under:
            print(0)

        elif not heap_over:
            print(-heapq.heappop(heap_under))

        elif not heap_under:
            print(heapq.heappop(heap_over))

        else:
            if heap_over[0] > heap_under[0]:
                print(-heapq.heappop(heap_under))

            elif heap_over[0] < heap_under[0]:
                print(heapq.heappop(heap_over))

            # 같을 때
            else:
                print(-heapq.heappop(heap_under))