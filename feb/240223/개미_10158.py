# w : 가로, h : 세로
w, h = map(int, input().split())

# 초기 개미 위치
start_w, start_h = map(int, input().split())

# 시간
t = int(input())

end_w = t + start_w
end_h = t + start_h

# 만약 end_w가 짝수면 나머지 자체가 답임
if (end_w // w) % 2 == 0:
    answer_w = end_w % w
# 홀수면 전체에서 나머지를빼야함
elif (end_w // w) % 2 == 1:
    answer_w = w - end_w % w

# 만약 end_h가 짝수면 나머지 자체가 답임
if (end_h // h) % 2 == 0:
    answer_h = end_h % h

# 홀수면 전체에서 나머지를빼야함
elif (end_h // h) % 2 == 1:
    answer_h = h - end_h % h

print(answer_w, answer_h)