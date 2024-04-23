import sys
input = sys.stdin.readline
n, k = map(int, input().split())
word = list(input())
# print(word)

cnt = 0
for i in range(n):
    if word[i] == 'P':
        # i번째 사람이 가져갈수있는 햄버거의 위치
        for j in range(i-k, i+k+1):
            # 범위 안에 있고 그게 햄버거이면
            if 0 <= j < n and word[j] == 'H':
                # 햄버거 먹음
                word[j] = 'X'
                cnt += 1
                break

# print(word)
print(cnt)