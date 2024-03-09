channel = int(input())
channel_str = str(channel)
m = int(input())

if m:
    breakdown = list(map(int, input().split()))
else:
    breakdown = []
# print(breakdown)

can_use = list(set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(breakdown))
# print(can_use)

# 기본값으로 현재 채널에서 가야하는 채널까지의 차를 잡음
# 이 값을 기준으로 나중에 나온 answer과 비교할듯
answer = abs(channel-100)

# 다부서졌으면
if not can_use:
    print(answer)
    exit()

max_use = max(can_use)
min_use = min(can_use)

last_change = False

new_answer = ''
# 채널번호를 제일 큰 자리수부터 하나씩 순회
for i in channel_str:
    # i가 breakdown에 없으면 -> 쓸수있는숫자면
    if int(i) not in breakdown:
        new_answer += i

    # 앞에서 부터 순회하다가 안맞는 자리가 발생
    else:
        if new_answer:
            # 1. 그 전 숫자를 없애고 그 근처 값들을 넣는 방법
            last_change = new_answer[:-1]
            last = int(new_answer[-1])
            # 그 다음 숫자는 제일 근처 숫자 넣기
            near = can_use[0]
            # 차이를 저장할 변수
            near_abs = float('inf')

            for j in can_use:
                # 순회하며 차이가 제일 적은 값을 near_abs에 넣을 예정
                if near_abs > abs(last - j):
                    near_abs = abs(last - j)
                    near = j

            # 차이가 제일 적은게 두개일수도있음
            near_ls = []
            for j in can_use:
                # 순회하며 차이가 제일 적은 값을 near_ls에 넣을 예정
                if near_abs == abs(last - j):
                    near_ls.append(j)
            # print(near_ls)

            # 경우가 하나면
            if len(near_ls) == 1:
                # 그 숫자가 채널의 같은 자리수보다 큰지 작은지 비교
                # 크면
                if near_ls[0] > last:
                    # 남은 수를 작은 수로 채워 넣음
                    last_change += str(near_ls[0])
                    left_len = len(channel_str) - len(last_change)

                    for _ in range(left_len):
                        last_change += str(min_use)
                # 작으면
                else:
                    # 남은 수를 큰 수로 채워 넣음
                    last_change += str(near_ls[0])
                    left_len = len(channel_str) - len(last_change)

                    for _ in range(left_len):
                        last_change += str(max_use)
                # # 완성
                # break

            # 두개면
            elif len(near_ls) == 2:
                # 작은거 넣기
                new_answer_1 = last_change
                new_answer_1 += str(min(near_ls))
                left_len = len(channel_str) - len(new_answer_1)
                for _ in range(left_len):
                    # 작은걸 넣었으면 남은 수는 큰걸로 채우기
                    new_answer_1 += str(max_use)

                # 큰거 넣기
                new_answer_2 = last_change
                new_answer_2 += str(max(near_ls))
                left_len = len(channel_str) - len(new_answer_2)
                for _ in range(left_len):
                    # 큰걸 넣었으면 남은 수는 작은걸로 채우기
                    new_answer_2 += str(min_use)

                # 차이가 더 적은 걸 new_answer에 넣기
                if abs(channel - int(new_answer_1)) > abs(channel - int(new_answer_2)):
                    last_change = new_answer_2

                else:
                    last_change = new_answer_1

                # # 완성
                # break

        # 2. 그 전 숫자 유지
        # 그 다음 숫자는 제일 근처 숫자 넣기
        near = can_use[0]
        # 차이를 저장할 변수
        near_abs = float('inf')

        for j in can_use:
            # 순회하며 차이가 제일 적은 값을 near_abs에 넣을 예정
            if near_abs > abs(int(i) - j):
                near_abs = abs(int(i) - j)
                near = j

        # 차이가 제일 적은게 두개일수도있음
        near_ls = []
        for j in can_use:
            # 순회하며 차이가 제일 적은 값을 near_ls에 넣을 예정
            if near_abs == abs(int(i) - j):
                near_ls.append(j)
        # print(near_ls)

        # 경우가 하나면
        if len(near_ls) == 1:
            # 그 숫자가 채널의 같은 자리수보다 큰지 작은지 비교
            # 크면
            if near_ls[0] > int(i):
                # 남은 수를 작은 수로 채워 넣음
                new_answer += str(near_ls[0])
                left_len = len(channel_str) - len(new_answer)

                for _ in range(left_len):
                    new_answer += str(min_use)
            # 작으면
            else:
                # 남은 수를 큰 수로 채워 넣음
                new_answer += str(near_ls[0])
                left_len = len(channel_str) - len(new_answer)

                for _ in range(left_len):
                    new_answer += str(max_use)
            # 완성
            break

        # 두개면
        elif len(near_ls) == 2:
            # 작은거 넣기
            new_answer_1 = new_answer
            new_answer_1 += str(min(near_ls))
            left_len = len(channel_str) - len(new_answer_1)
            for _ in range(left_len):
                # 작은걸 넣었으면 남은 수는 큰걸로 채우기
                new_answer_1 += str(max_use)

            # 큰거 넣기
            new_answer_2 = new_answer
            new_answer_2 += str(max(near_ls))
            left_len = len(channel_str) - len(new_answer_2)
            for _ in range(left_len):
                # 큰걸 넣었으면 남은 수는 작은걸로 채우기
                new_answer_2 += str(min_use)

            # 차이가 더 적은 걸 new_answer에 넣기
            if abs(channel - int(new_answer_1)) > abs(channel - int(new_answer_2)):
                new_answer = new_answer_2

            else:
                new_answer = new_answer_1

            # 완성
            break
# print(answer, new_answer)

button = abs(channel - int(new_answer)) + len(channel_str)
# print(answer, button)
if last_change:
    button_2 = abs(channel - int(last_change)) + len(channel_str)
    print(min(answer, button, button_2))
else:
    print(min(answer, button))
