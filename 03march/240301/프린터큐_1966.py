from collections import deque

T = int(input())

for test_case in range(1, T+1):
    # n : 문서의 갯수, m : 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지
    n, m = map(int, input().split())

    ls = list(map(int, input().split()))

    # 현재 idx와 값을 저장
    new_ls = deque([])
    for idx, val in enumerate(ls):
        new_ls.append([idx, val])
    # print(new_ls)

    cnt = 0
    while 1:
        # 맨 앞의 ls를 뺌
        first = new_ls.popleft()

        # 모든 ls를 돌며
        for i in new_ls:
            # 중요도가 더 큰게 있다면
            if first[1] < i[1]:
                # 뒤에다 다시 append
                new_ls.append(first)
                break

        # 반복문을 다 돌았는데도 break가 안걸리면 그게 중요도가 제일 큰것이었음 -> 빠졌음
        else:
            cnt += 1
            # 내가 찾는 ls가 빠진거였으면
            if first[0] == m:
                break


    print(cnt)