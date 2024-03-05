a, b, v = map(int, input().split())

# 목표
p = v-a

# 하루에 올라갔다가 미끄러지는 길이
day = a-b

# 목표까지 얼마나 걸리는지
answer = p // day

# 근데만약 딱 안나눠 떨어지면 1 더해줌
if p % day != 0:
    answer += 1

# 목표 도착 후 다음날 아침에 올라가면 끝
print(answer+1)