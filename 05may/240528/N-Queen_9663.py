n = int(input())

def tf(row, col):
    visited = [[0] * n for _ in range(n)]

    # 방문한 곳을 미리 찍음
    for p in path:
        # path에 들어있는 점들이 방문한 곳이면
        visited[p[0]][p[1]] = 1

    # 위쪽 같은 열에 방문 표시
    for i in range(row):
        if visited[i][col]:
            return False

    # 오른쪽 대각선
    for j in range(n-col):
        if visited[row-j][col+j]:
            return False

    # 왼쪽 대각선
    for k in range(col+1):
        if visited[row-k][col-k]:
            return False

    # 전부 통과했으면
    return True

def back(row, cnt):
    global ans
    # 종료 조건
    if cnt == n:
        ans += 1
        return

    # 행은 다음 행으로 고정
    # 열만 처음부터 n까지 찾아보기
    for col in range(n):
        # 다음 queen을 놓을 수 있는 위치인지 파악
        if tf(row, col):
            # 가능하면
            path.append([row, col])
            back(row+1, cnt + 1)
            path.pop()

path = []
ans = 0
back(0, 0)
print(ans)