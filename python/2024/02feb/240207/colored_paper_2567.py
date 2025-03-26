import pprint

'''
1. arr을 101x101인 0행렬을 만들어 input으로 받은 좌표들을 기준으로 1 대입
2. arr의 모든 좌표를 순회하며 1을 찾아 1의 상하좌우를 확인 후 0이 있는 갯수만큼 cnt += 1
'''

N = int(input())

ls = [list(map(int, input().split())) for _ in range(N)]

# index 편하게 하기 위해 한칸 더 줌
arr = [[0] * (101) for _ in range(101)]

# # pprint를 사용하여 이쁘게 출력
# # 근데 잘안됨
# pp = pprint.PrettyPrinter(width=200, compact=True)
# pp.pprint(arr)

# arr에 색 채우기
# ls안의 왼쪽 아래 좌표들을 순회
for location in ls:
    # 왼쪽 아래 좌표의 x값을 기준으로 10만큼
    for x in range(location[0], location[0] + 10):
        # y값을 기준으로 10만큼
        for y in range(location[1], location[1] + 10):
            arr[x][y] = 1

# pp = pprint.PrettyPrinter(width=100, compact=True)
# pp.pprint(arr)

cnt = 0

# arr의 모든 좌표를 순회
for i in range(101):
    for j in range(101):
        # 어떤 좌표가 1 이면 그 상하좌우를 살펴 0이 있는 갯수만큼 cnt += 1
        # 상
        if i > 0 and arr[i-1][j] != arr[i][j]:
            cnt += 1
        # 하
        if i+1 < 101 and arr[i+1][j] != arr[i][j]:
            cnt += 1
        # 좌
        if j > 0 and arr[i][j-1] != arr[i][j]:
            cnt += 1
        # 우
        if j+1 < 101 and arr[i][j+1] != arr[i][j]:
            cnt += 1

# 이러면 1을 기준으로 할 때랑 0을 기준으로 할 때 두번 체크되기 때문에 2를 나눠 줍니당
print(cnt // 2)