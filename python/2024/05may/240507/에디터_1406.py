# 왼쪽과 오른쪽으로 나눔
ls_left = list(input())
ls_right = []

n = int(input())
arr = [input().split() for _ in range(n)]
# print(arr)

for i in range(n):
    # L이면
    if arr[i][0] == 'L':
        # 왼쪽에 값이 있을 때
        if ls_left:
            # 왼쪽에서 하나빼서 오른쪽으로 넘김
            ls_right.append(ls_left.pop())

    # D이면
    elif arr[i][0] == 'D':
        # 오른쪽에 값이 있을 때
        if ls_right:
            # 오른쪽에서 하나 빼서 왼쪽으로 넘김
            ls_left.append(ls_right.pop())

    # B이면
    elif arr[i][0] == 'B':
        # 왼쪽에 뭐가 있으면
        if ls_left:
            ls_left.pop()

    # P이면
    elif arr[i][0] == 'P':
        # 글자 추가
        ls_left.append(arr[i][1])

# print(ls_left)
# print(ls_right)

print(''.join(ls_left) + ''.join(ls_right[::-1]))