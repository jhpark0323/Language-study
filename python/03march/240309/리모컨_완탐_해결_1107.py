N = int(input()) # 목표 채널
M = int(input()) # 고장난 버튼 개수
if M == 0:
    M_lst = []
else:
    M_lst = list(map(int, input().split())) # 고장난 버튼

min_click = abs(N-100)

for cl_num in range(1000001):
    for num in str(cl_num):
        if int(num) in M_lst:
            break
    else:
        min_click = min(min_click, len(str(cl_num))+abs(cl_num-N))

print(min_click)