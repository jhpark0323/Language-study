from collections import deque

def bfs(n):
    visited = set()
    # n 방문
    visited.add(n)
    q = deque([(n, 0)])

    while q:
        current_n, time = q.popleft()
        # print('current_n, time : ', current_n, time)

        # 정확하게 나눠 떨어지면 끝
        if current_n == 0:
            return time


        for next in (current_n - 5, current_n - 3):
            # 방문하지 않았다면
            if next not in visited:
                visited.add(next)
                q.append((next, time+1))
                # 다음이 0이면 거기서 끝
                if next == 0:
                    return time+1
                # print('visited :', visited)
                # print('q :', q)
                # print()

        # q안의 모든 요소들이 음수일 때
        cnt = 0
        for i in range(len(q)):
            if q[i][0] < 0:
               cnt += 1
        if cnt == len(q):
            return -1

n = int(input())

print(bfs(n))