'''
30의 배수 판정법
10, 3
'''

n = list(map(int, input()))
# print(n)

answer = -1

# 30의 배수이면
# 10의 배수를 만들 수 있음
if 0 in n:
    # 3의 배수 판정법
    if sum(n) % 3 == 0:
        # 제일큰걸 만들어야 하기에 내림차순함
        n.sort(reverse=True)
        # answer에 하나씩 추가해줌 str형태로
        answer = ''
        for i in n:
            answer += str(i)

print(answer)