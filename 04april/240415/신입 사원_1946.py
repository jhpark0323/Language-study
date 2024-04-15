T = int(input())

for _ in range(T):
    # 지원자의 숫자
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(reverse=True)
    # print(arr)

    # 1부터 n까지의 모든 등수를 나타내는 ls
    rank = set(i for i in range(1, n+1))
    minus = set()
    for i in range(n):
        if arr[i][1] == 1:
            # 1이나온 idx 찾기
            idx = i
            break
        # 1이 아니면
        else:
            minus.add(arr[i][1])
    # print(minus)

    new_ls = list(rank - minus)
    # print(new_ls)

    cnt = 0
    new_set_idx = 0
    ls = []
    for i in range(idx, n):
        if arr[i][1] == new_ls[new_set_idx] and arr[i][1] not in ls:
            cnt += 1
            new_set_idx += 1
        else:
            ls.append(arr[i][1])

    print(cnt)

'''
1
5
1 5
2 3
3 4
4 2
5 1
'''