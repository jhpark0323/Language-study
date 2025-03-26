from collections import deque

n = int(input())
arr = [input().split()[::-1] for _ in range(n)]
written = input().split()
# print(arr)

# 적혀진 문장을 순회
for i in written:
    # arr 순회
    for parrot in arr:
        # 적혀진 문장과 같은게 나오면
        if parrot and parrot[-1] == i:
            parrot.pop()
            break

    # arr을 순회해도 같은게 안나오면
    else:
        print('Impossible')
        exit()

for i in arr:
    # 하나라도 비어있지 않으면
    if i:
        print('Impossible')
        exit()

print('Possible')