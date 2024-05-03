from pprint import pprint
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# pprint(arr)

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def back(r, c, cnt, total):
    global ans
    # 종료조건
    if cnt == 4:
        # print('total :', total)
        # print('path :', path)
        if ans < total:
            ans = total
        return

    for dij in range(4):
        next_r = r + di[dij]
        next_c = c + dj[dij]
        # 범위안에 있고 방문하지 않았으면
        if 0 <= next_r < n and 0 <= next_c < m and not visited[next_r][next_c]:
            # 방문표시 하고
            visited[next_r][next_c] = True

            # # 디버깅용 거리
            # path.append(arr[next_r][next_c])

            back(next_r, next_c, cnt+1, total+arr[next_r][next_c])
            # 원상복구
            visited[next_r][next_c] = False

            # # 디버깅용
            # path.pop()

# ㅗ모양을 위 방법으로 찾을 수 없음
def another(r, c):
    global ans
    # +의 모양
    new_ans = arr[r][c]
    cnt = 0
    for i in range(4):
        # 범위안에 있을 때
        if 0 <= r+di[i] < n and 0 <= c+dj[i] < m:
            new_ans += arr[r+di[i]][c+dj[i]]
            cnt += 1

    # cnt가 3보다 작으면 그냥 return
    if cnt < 3:
        return

    # 3칸이면
    if cnt == 3:
        # 비교
        if ans < new_ans:
            ans = new_ans
        return

    # 4칸이면
    if cnt == 4:
        # 제일 작은거 하나만빼서 최댓값 만들기
        new_ans -= min(arr[r-1][c], arr[r+1][c], arr[r][c-1], arr[r][c+1])

        # 비교
        if ans < new_ans:
            ans = new_ans
        return

ans = 0
# 전체를 다 돌며 시작위치를 순회
for row in range(n):
    for col in range(m):
        visited = [[False] * m for _ in range(n)]
        visited[row][col] = True
        # 디버깅용 거리 ls
        # path = []
        back(row, col, 1, arr[row][col])
        another(row, col)

print(ans)