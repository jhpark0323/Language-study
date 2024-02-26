T = int(input())

for tc in range(T):
    # 호텔의 층 수, 각 층의 방 수, 몇 번째 손님
    h, w, n = map(int, input().split())

    # 1호실부터 배정
    if n % h == 0:
        rooms = n // h
    else:
        rooms = n // h + 1

    # 층
    if n % h == 0:
        floor = h
    else:
        floor = n % h

    print(floor * 100 + rooms)