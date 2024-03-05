memo = {}

def f(floor, ho):
    # 이미 계산되었으면 반환
    if (floor, ho) in memo:
        return memo[(floor, ho)]

    # 0층에는 ho만큼의 인원이 삼
    if floor == 0:
        memo[(floor, ho)] = ho
        return ho

    if ho == 0:
        memo[(floor, ho)] = 0
        return 0

    # 1호에는 1명이 삼
    if ho == 1:
        memo[(floor, ho)] = 1
        return 1

    memo[(floor, ho)] = f(floor, ho-1) + f(floor-1, ho)
    return memo[(floor, ho)]


'''
아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
'''

T = int(input())

for test_case in range(T):
    # 층
    floor = int(input())
    # 호
    ho = int(input())

    print(f(floor, ho))