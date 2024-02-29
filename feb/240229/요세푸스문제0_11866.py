n, k = map(int, input().split())

p = [i for i in range(1, n+1)]
answer = []
idx = 0  # 회전할 때 사용할 인덱스 초기화

for _ in range(n):
    idx = (idx + k - 1) % len(p)  # k번째 원소의 인덱스 계산
    answer.append(p.pop(idx))  # 해당 인덱스의 원소를 추출하여 결과에 추가

# 결과 문자열 생성
ans = '<' + ', '.join(map(str, answer)) + '>'
print(ans)
