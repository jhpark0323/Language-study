from pprint import pprint

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


# 학생 찾기 함수
def find_stu(o_ls):
    global ans

    # 장애물 넣기
    for i in o_ls:
        arr[i[0]][i[1]] = 'O'

    # 학생 찾기
    for i in range(n):
        for j in range(n):
            # 선생님 나오면
            if arr[i][j] == 'T':
                # 4방향을 돌아서 학생을 찾아봄
                for dij in range(4):
                    next_i = i + di[dij]
                    next_j = j + dj[dij]

                    # 그 방향으로 쭉 앞으로감 장애물 나올 때 까지
                    while 0 <= next_i < n and 0 <= next_j < n:
                        # 장애물을 만나면 while문 종료하고 다음 방향으로 넘어감
                        if arr[next_i][next_j] == 'O':
                            break
                        # 학생을 만나면 끝
                        elif arr[next_i][next_j] == 'S':

                            # 원상복구
                            for i in o_ls:
                                arr[i[0]][i[1]] = 'X'
                            return

                        # 그냥 통로면 1칸더 가서 그 뒤를 봄
                        next_i += di[dij]
                        next_j += dj[dij]

    # 모든 경우를 다봐도 학생을 못찾으면
    # ans = 'YES'
    # pprint(arr)
    exit(print('YES'))
    return


def back(cnt):
    # 종료조건
    if cnt == 3:
        # print(obstacle_ls)
        find_stu(obstacle_ls)
        return

    # arr을 돌며 O(장애물) 대입
    for row in range(n):
        for col in range(n):
            # 통로이고 o_ls에 없는 거면
            if arr[row][col] == 'X' and [row, col] not in obstacle_ls:
                obstacle_ls.append([row, col])
                back(cnt+1)
                obstacle_ls.pop()


n = int(input())
arr = [list(input().split()) for _ in range(n)]
obstacle_ls = []
ans = 'NO'
back(0)
print(ans)