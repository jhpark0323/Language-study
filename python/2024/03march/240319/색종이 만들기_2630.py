'''
분할정복으로 할 때 마다 각각이 풀로차있는지 확인?
'''

def divide_conquer(arr, n):
    global white
    global blue

    # 세어봄
    color_paper = 0
    for i in arr:
        color_paper += sum(i)

    # 흰 종이 이면
    if color_paper == 0:
        white += 1
        return

    # 파란 종이 이면
    if color_paper == n**2:
        blue += 1
        return

    arr_1 = [row[:n//2] for row in arr[:n//2]]
    arr_2 = [row[n//2:] for row in arr[:n//2]]
    arr_3 = [row[:n//2] for row in arr[n//2:]]
    arr_4 = [row[n//2:] for row in arr[n//2:]]

    divide_conquer(arr_1, n//2)
    divide_conquer(arr_2, n//2)
    divide_conquer(arr_3, n//2)
    divide_conquer(arr_4, n//2)


n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

divide_conquer(paper, n)

print(white)
print(blue)