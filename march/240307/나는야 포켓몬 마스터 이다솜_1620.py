n, m = map(int, input().split())

dogam = [input() for _ in range(n)]
# print(dogam)

question = [input() for _ in range(m)]

for i in question:
    # 숫자면
    if i.isdigit():
        print(dogam[int(i)-1])

    else:
        print(dogam.index(i) + 1)