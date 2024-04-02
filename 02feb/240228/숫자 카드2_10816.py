import sys

# 숫자 카드의 개수를 세는 함수
def count_cards(cards):
    card_counts = {}
    for card in cards:
        if card in card_counts:
            card_counts[card] += 1
        else:
            card_counts[card] = 1
    return card_counts

# 입력 받기
n = int(sys.stdin.readline().strip())
cards = list(map(int, sys.stdin.readline().strip().split()))

# 숫자 카드 개수 세기
card_counts = count_cards(cards)

# 찾고자 하는 숫자들을 받고 카운트 출력
m = int(sys.stdin.readline().strip())
targets = list(map(int, sys.stdin.readline().strip().split()))

for target in targets:
    if target in card_counts:
        print(card_counts[target], end=' ')
    else:
        print(0, end=' ')
