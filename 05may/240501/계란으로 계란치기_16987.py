import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def backtracking(index):
    global max_cnt
    # 종료조건
    if index == n:
        # print(array)
        cnt = 0
        for i in range(n):
            # 깨졌으면
            if arr[i][0] <= 0:
                cnt += 1

        if max_cnt < cnt:
            max_cnt = cnt
        return

    # 무조건 처음부터 시작
    # n개를 다 돌면서 할거임
    # 근데 어떤 계란을 깨냐에 따라 배열이 계속 바뀔 예정
    for i in range(n):
        first_s, first_w = arr[index][0], arr[index][1]
        second_s, second_w = arr[i][0], arr[i][1]

        origin_f_s, origin_f_w = first_s, first_w
        origin_s_s, origin_s_w = second_s, second_w
        # print('first_s :', first_s)

        # 첫번째 계란이 깨졌으면
        if first_s <= 0:
            backtracking(index + 1)
            return

        # 첫번째 계란과 두번째 계란이 같을 수는 없음
        # 깨진 계란은 못깸
        if second_s <= 0:
            continue


        if i == index:
            # 마지막일때는 백트를 한번 못해서 그냥 여기서 계산 해줌
            if index == n-1:
                cnt = 0
                for i in range(n):
                    # 깨졌으면
                    if arr[i][0] <= 0:
                        cnt += 1

                if max_cnt < cnt:
                    max_cnt = cnt
                return
            continue
            # print('second_s :', second_s)

        # 계란 깨기
        first_s -= second_w
        second_s -= first_w

        # 계란 update
        arr[index] = [first_s, first_w]
        arr[i] = [second_s, second_w]
        # print(arr)

        backtracking(index+1)
        arr[index] = [origin_f_s, origin_f_w]
        arr[i] = [origin_s_s, origin_s_w]

max_cnt = 0
backtracking(0)
print(max_cnt)