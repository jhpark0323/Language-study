from collections import deque

# 딱지놀이의 총 라운드 수
n = int(input())

# 딱지 갯수와 딱지들
arr = [list(map(int, input().split())) for _ in range(2*n)]

# A의 카드들
a = []
for i in range(0, 2*n, 2):
    # 첫번째 원소는 갯수 -> 필요없어 보임
    # 안에 넣을 때도 q의 형태로 넣음 -> 35번째 줄 때문에
    a.append(deque(sorted(arr[i][1:], reverse=True)))

# B의 카드들
b = []
for i in range(1, 2*n, 2):
    # 첫번째 원소는 갯수 -> 필요없어 보임
    # 안에 넣을 때도 q의 형태로 넣음 -> 36번째 줄 때문에
    b.append(deque(sorted(arr[i][1:], reverse=True)))

# print(a)
# print(b)

a_q = deque(a)
b_q = deque(b)

for i in range(n):
    # 각 라운드의 카드는 popleft
    a_round = a_q.popleft()
    b_round = b_q.popleft()
    # a_round랑 b_round가 비기 전까지
    while a_round and b_round:
        a_card = a_round.popleft()
        b_card = b_round.popleft()
        # print(a_card, b_card)

        # 각 라운드에서 더 큰 카드가 나오면 반환후 break
        if a_card > b_card:
            print('A')
            break
        elif b_card > a_card:
            print('B')
            break

    # for else가 있으면 while else도 있겠지??
    else:
        # while문을 다돌았을 경우 -> 가지고 있던 카드를 다썻지만 그때까지는 같았음
        # a_round와 b_round가 둘다 비어있을 때
        if not a_round and not b_round:
            # 비김
            print('D')
        # a_round에 원소가 남아있을 경우
        elif a_round:
            print('A')

        # b_round에 원소가 남아있을 경우
        else:
            print('B')

    # 있따!!!!!!!!!