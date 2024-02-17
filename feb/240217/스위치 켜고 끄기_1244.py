# 스위치 갯수
n = int(input())
# 스위치 상태 ls
switch = list(map(int, input().split()))
# 학생 수
stu_n = int(input())
# 학생 성별, 받은 수
stu_ls = [list(map(int, input().split())) for _ in range(stu_n)]


# 스위치 켜고 끄기
# 스위치만 켜고 끌거기 때문에 따로 return값은 없음
def turn_on_off(idx):
    # switch라는 ls를 직접 바꿔야하기에 전역변수 설정
    global switch

    # switch는 1번부터 시작하고 index는 0부터 시작하므로 1을 빼줌
    if switch[idx - 1] == 1:
        switch[idx - 1] = 0
    # 0이었으면 1로
    else:
        switch[idx - 1] = 1

# switch의 상태를 변화시켯기에 따로 return은 안함
def switch_status(gender, given_num):
    global switch
    # 남학생이면
    if gender == 1:
        # 스위치 번호가 받은 번호의 배수이면
        for switch_num in range(1, n+1):
            if switch_num % given_num == 0:
                # 스위치 상태 변경
                turn_on_off(switch_num)
                # print(switch)
    # 여학생이면
    else:
        # 받은 스위치 상태 바꾸기
        turn_on_off(given_num)
        # 좌우 index 변화할 애들 기준정해줌
        given_left = given_num
        given_right = given_num

        while 1:
            # 주어진 곳의 좌우
            given_left -= 1
            given_right += 1
            # 범위안에 있고 좌우가 같은 상태일 때
            if 0 <= given_left-1 < n and 0 <= given_right-1 < n and switch[given_left-1] == switch[given_right-1]:
                # 좌우의 상태를 바꿈
                turn_on_off(given_left)
                turn_on_off(given_right)
                # print(switch)

            # 범위안에 없거나 좌우가 다른 상태면 break
            else:
                break

for i in stu_ls:
    # stu_ls에서 각각의 성별과 주어진 번호를 꺼냄
    gender, given_num = i[0], i[1]
    switch_status(gender, given_num)

# 출력도 개까다롭게하네
size = 20

for i in range(0, n, size):
    print(*switch[i:i+size])