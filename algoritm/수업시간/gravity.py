n = int(input())  # 상자가 쌓여있는 가로 길이
box = list(map(int, input().split()))

max_v = 0  # 가장 큰 낙차

for i in range(n-1):  # for i : 0 -> n-2, i 낙차를 구할 위치
    cnt = 0  # 오른쪽에 있는 더 낮은 높이의 개수
    for j in range(i+1, n):  # for j : i+1 -> n-1
        if box[i] > box[j]:
            cnt += 1
    if max_v <= cnt:
        max_v = cnt

print(max_v)
