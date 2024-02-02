n = int(input())

hansu = 0

'''
1. n을 받아서 전부 다 돌려봄 -> 100이상부터 돌려도 될듯 (한자리수, 두자리수는 무조건 전부 한수임)
2. all_num을 각자리를 원소로하는 list를 만들까?
3. list의 연속된 두원소들의 차이가 일정하면 등차수열이겠네
'''


# 한자리수, 두자리수는 무조건 전부 한수임
if n < 100:
    hansu = n

# 나머지 100부터 시작
else:
    # 100전까지는 다 한수기때문에 n이100을 넘어가면 기본적으로 99개 먹고 시작함
    hansu = 99
    for all_num in range(100, n+1):
        # 각자리를 원소로하는 num_li 생성
        num_ls = [int(i) for i in str(all_num)]
        # print(num_ls)

        difference = []
        # 0부터 num_ls의 길이 -1만큼 반복 -> index로 앞뒤 두개 비교 할거라서
        for idx in range(len(num_ls)-1):
            # 앞과 뒤의 차이를 difference에 append
            difference.append(num_ls[idx+1] - num_ls[idx])

        # 차이 값들이 들어있는 list의 집합을 구해 중복을 제거하고 그 원소의 갯수가 1이면 한수 += 1
        if len(set(difference)) == 1:
            # print(num_ls)
            hansu += 1


print(hansu)