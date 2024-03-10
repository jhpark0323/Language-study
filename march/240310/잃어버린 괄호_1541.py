# -로 split해서 맨 처음 숫자에서 나머지 split 된것들의 합을 빼줌
ls = input().split('-')
# print(ls)

# ls의 첫번째 값이 숫자면 answer에 저장
if ls[0].isdigit():
    answer = int(ls[0])

# ls의 첫번째 값이 +로 연결되어있으면
else:
    # +로 split한 후에 다 더함
    answer = list(map(int, ''.join(ls[0]).split('+')))
    answer = sum(answer)
    # exit()

# ls의 1번째 index부터 순회
for i in ls[1:]:
    # 각각을 +을 기준으로 split
    new = list(map(int, i.split('+')))
    # 다 더해줌
    new_sum = sum(new)
    # answer에 -= 해줌
    answer -= new_sum

print(answer)