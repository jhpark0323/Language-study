
'''
수빈이가 갈 수 있는 방향이 3곳이고 그때마다 경우를 탐색해야 하기 때문에
현재 위치에서 부터 근처부터 탐색하여 최소값을 찾아야 하기에
bfs를 사용
'''

from collections import deque

# n : 수빈, k : 동생 위치
n, k = map(int, input().split())

def bfs(n, k):
    # 1차원에 있으므로 visited를 집합으로 놓음
    visited = set([n])
    # q에는 각각 몇번 진행되었는지를 알아야 하므로 위치정보와 몇번진행했는지에 대한 정보를 같이 넣는다.
    q = deque([[n, 0]])

    while q:
        # 먼저 현재위치와 몇번인지를 뽑는다
        current, time = q.popleft()

        # 현재 위치가 동생의 위치와 같다면 종료
        if current == k:
            return time

        # 다음 위치는 다음 세개중에 있음
        for next in (current-1, current+1, 2*current):
            # 방문하지 않았고, 범위안에 있으면
            if next not in visited and 0 <= next <= 100000:
                # 방문표시 후
                visited.add(next)
                # q에 append
                q.append([next, time+1])

if n <= k:
    print(bfs(n, k))
else:
    print(n-k)