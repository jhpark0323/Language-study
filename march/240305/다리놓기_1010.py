import math

'''
동쪽에서 서쪽의 갯수만큼 고르기만 하면 됨
그 경우의 경우의수는 1밖에없음 -> 안겹치게 하는게 하나거든
'''

T = int(input())

for test_case in range(T):
    # w : 서쪽, e : 동쪽 (w <= e)
    w, e = map(int, input().split())

    # 걍 조합임
    answer = math.comb(e, w)

    print(answer)