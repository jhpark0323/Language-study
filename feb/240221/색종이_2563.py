num = int(input())

black_paper = [list(map(int, input().split())) for _ in range(num)]

# print(black_paper)

arr = [[0] * 100 for _ in range(100)]

# print(arr)
for paper in range(num):
    dot_x = black_paper[paper][0]
    for row in range(10):
        dot_y = black_paper[paper][1]
        for col in range(10):
            if (dot_x < 100) | (dot_y < 100):
                if arr[dot_x][dot_y] == 0:
                    arr[dot_x][dot_y] = 1
            dot_y += 1
        dot_x += 1

# print(arr)

answer = 0
for i in arr:
    answer += sum(i)

print(answer)
