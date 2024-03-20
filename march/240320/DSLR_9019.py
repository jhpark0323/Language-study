import sys
from collections import deque

ipt = sys.stdin.readline

def bfs():
    visited = set()
    visited.add(a)
    q = deque([[a, '']])

    while q:
        current, command = q.popleft()
        # ls.append(command)
        # print(current)
        # 기저 조건
        if current == b:
            return command

        # 1. 2배
        if ((current*2) % 10000) not in visited:
            q.append([current*2 % 10000, command + 'D'])
            visited.add(current*2 % 10000)

        # 2. n-1저장
        # 0일때는
        if current == 0:
            # 0이 아직 방문 안한 곳이면
            if 9999 not in visited:
                q.append([9999, command + 'S'])
                visited.add(9999)
        # 0이 아닐때는
        else:
            # 방문 안했으면
            if (current-1) not in visited:
                q.append([current-1, command + 'S'])
                visited.add(current-1)

        # 3, 4번째는 무조건 4자리라 생각하고 풀어야 맞음
        # ex) 123 -> 0123, 123 : L -> 1230
        # -> 문제 설명이 이상한거 같은데 나만 그런가
        # 3. 왼편으로 회전
        if (current*10 + (current//1000)) % 10000 not in visited:
            q.append([(current*10 + (current//1000)) % 10000, command + 'L'])
            visited.add((current*10 + (current//1000)) % 10000)

        # 4. 오른쪽으로 회전
        if (current//10 + (current%10) * 1000) % 10000 not in visited:
            q.append([(current//10 + (current%10) * 1000) % 10000, command + 'R'])
            visited.add((current//10 + (current%10) * 1000) % 10000)


T = int(ipt().strip())

for test_case in range(T):
    a, b = map(int, ipt().strip().split())
    # print(a, b)

    # ls = []
    answer = bfs()
    # print(ls[-1])
    print(answer)