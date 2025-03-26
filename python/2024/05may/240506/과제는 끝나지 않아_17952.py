n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)

ans = 0
stack = []
for hw in range(n):
    # 과제가 있다면
    if arr[hw][0]:
        # 1분만에 끝나는거면
        if arr[hw][2] == 1:
            ans += arr[hw][1]
        # 아니면
        else:
            # 새로운 과제점수, 시간
            stack.append([arr[hw][1], arr[hw][2]-1])

    # 과제가 없을때
    else:
        # 앞에 하던 과제가 있으면
        if stack:
            now_hw_score, now_hw_time = stack.pop()
            # 1분 감소
            now_hw_time -= 1
            # 시간이 끝났으면
            if now_hw_time == 0:
                ans += now_hw_score
            # 시간이 더 남았으면
            else:
                stack.append([now_hw_score, now_hw_time])

print(ans)