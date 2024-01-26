n = int(input())

words = [input() for _ in range(n)]

# print(words)

# words list를 반복
for word in words:
    # 새로운 word가 시작될 때 ls를 초기화
    ls = []
    # word의 각각을 char로 둠
    for char in word:
        # 처음 반복문 돌 때는 무조건 추가
        if len(ls) == 0:
            ls.append(char)
        # char이 ls에 없거나 ls의 마지막과 char이 같으면 ls에 char 추가
        elif (char not in ls) | (char == ls[-1]):
            ls.append(char)
        # 아니면 총 갯수에서 하나씩 빼기
        else:
            n -= 1
            break

    # print(ls)

print(n)