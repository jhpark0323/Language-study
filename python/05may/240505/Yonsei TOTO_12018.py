n, m = map(int, input().split())
pl = []
mile = []
for _ in range(n):
    pl.append(list(map(int, input().split())))
    mile.append(list(map(int, input().split())))

# print(pl)
# print(mile)

cnt = 0
need_least_mile = []
for i in range(n):
    # 만약 과목에 신청한 사람 수 보다 과목의 수강인원이 더 많으면
    if pl[i][0] < pl[i][1]:
        # 마일리지 1만 줌
        m -= 1
        # 마일리지가 음수가 되면
        if m < 0:
            # 끝
            exit(print(cnt))
        # 한과목 추가
        cnt += 1

    else:
        # 과목당 수강생들이 쓴 마일리지를 내림차순 정렬
        mile[i].sort(reverse=True)
        # 수강인원
        num_stu = pl[i][1]
        # 수강인원의 마지막사람 mile append
        need_least_mile.append(mile[i][num_stu-1])
# print(need_least_mile)

# 오름차순 정렬
need_least_mile.sort()

# need_least_mile를 돌며 순회
for i in need_least_mile:
    m -= i
    # 마일리지를 썻는데 0보다 크게 남아있으면
    if m >= 0:
        cnt += 1
    # 마일리지 다 썼으면
    else:
        break
print(cnt)