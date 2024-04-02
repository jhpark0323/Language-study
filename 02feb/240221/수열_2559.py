from collections import deque

# n : 온도를 측정한 전체 날짜의 수, k : 합을 구하기 위한 연속적인 날짜
n, k = map(int, input().split())

# 온도 수열
ls = list(map(int, input().split()))

# q에는 처음 연속k일을 list로 할당
q = deque(ls[:k])
# print(q, sum(q))

# 맨처음 k일의 합
sum_q = sum(q)

# 최종합
max_sum = sum_q

for i in range(k, n+1):
    if i == n:
        break
    # 하나 더해주고 맨앞에꺼 빼기
    q.append(ls[i])
    sum_q = sum_q - q.popleft() + q[-1]
    if max_sum < sum_q:
        max_sum = sum_q

print(max_sum)