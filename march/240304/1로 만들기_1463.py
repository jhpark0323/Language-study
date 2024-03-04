from collections import deque

def bfs(x):
    # 1차원에 있으므로 visited를 집합으로 놓음
    visited = set([x])
    # q에는 각각 몇번 진행되었는지를 알아야 하므로 위치정보와 몇번진행했는지에 대한 정보를 같이 넣는다.
    q = deque([[x, 0]])

    while q:
        # 현재 위치와 몇번째인지 뽑아옴
        current, time = q.popleft()

        # 1이 되면 종료
        if current == 1:
            return time

        # 다음 위치는 세개중에 가능한 곳을 고름
        ls = []
        if current % 3 == 0:
            ls.append(current//3)
            # x //= 3
        if current % 2 == 0:
            ls.append(current//2)
            # x //= 2
        ls.append(current-1)

        # 다음위치로 갈 수 있는 곳 ls를 순회
        for next in ls:
            if next not in visited and 0 <= next <= 1000000:
                visited.add(next)
                q.append([next, time+1])


'''     
1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.
'''

n = int(input())

print(bfs(n))