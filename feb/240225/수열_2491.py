n = int(input())
# 수열
an = list(map(int, input().split()))

# 커지는 전부 나열한 ls
an_bigger = [1] * n
# 작아지는 수열 전부 나열한 ls
an_smaller = [1] * n

# 커지는 수열 조사
for i in range(1, n):
    # 전항보다 현재 항이 더크면
    if an[i-1] <= an[i]:
        # an_bigger의 전항의 원소에서 1 더해줌
        an_bigger[i] = an_bigger[i-1] + 1


# 작아지는 수열 조사
for i in range(1, n):
    # 전항보다 현재 항이 더크면
    if an[i-1] >= an[i]:
        # an_smaller의 전항의 원소에서 1 더해줌
        an_smaller[i] = an_smaller[i-1] + 1

print(max(max(an_bigger), max(an_smaller)))