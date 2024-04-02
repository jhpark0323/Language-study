arr = [input() for _ in range(5)]

# print(arr)

# arr에 제일 길이가 긴 글자
longest = max(arr, key=len)
# print(longest)


for i in range(len(arr)):
    if len(arr[i]) != longest:
        arr[i] += ' '*(len(longest) - len(arr[i]))
# print(arr)

answer = ''

for row in range(len(longest)):
    for col in range(5):
        if arr[col][row] != ' ':
            answer += arr[col][row]
            

print(answer)