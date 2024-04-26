n = int(input())
dough, topping = map(int, input().split())
dough_calorie = int(input())
topping_calorie_ls = [int(input()) for _ in range(n)]
# print(topping_calorie)

topping_calorie_ls.sort()

# 기준은 토핑을 하나도 고르지 않았을 때
max_ans = dough_calorie // dough
topping_calorie = 0
topping_num = 0
# 토핑 칼로리중 큰거 하나씩 빼서 비교
while topping_calorie_ls:
    # 토핑 칼로리는 끝에서 하나씩 빼서 더함
    topping_calorie += topping_calorie_ls.pop()
    topping_num += 1
    ans = (dough_calorie + topping_calorie) // (dough + topping * topping_num)
    if max_ans < ans:
        max_ans = ans


print(max_ans)