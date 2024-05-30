import sys
input = sys.stdin.readline
n, c, w = map(int, input().split())

ls = []
max_tree = 0
for _ in range(n):
    tree = int(input())
    ls.append(tree)
    if max_tree < tree:
        max_tree = tree
# print(ls)
# print(max_tree)

max_cost = 0
for tree_l in range(1, max_tree+1):
    cost = 0
    for each_tree in ls:
        tree_c = each_tree // tree_l

        new_cost = 0
        # 아래 for문에 안들어 갈 수도 있기 때문에 미리 설정을 해둠
        # 아래에서 i를 쓰기 때문
        i = 0
        # 잘랐을때 이득인지 계산
        for i in range(tree_c+1):
            new_new_cost = i * tree_l * w - i * c

            if new_cost < new_new_cost:
                new_cost = new_new_cost

        # 나눠서 떨어지면 마지막 한번 덜자를 수 있음
        if each_tree % tree_l == 0:
            new_new_cost = i * tree_l * w - (i-1) * c

            if new_cost < new_new_cost:
                new_cost = new_new_cost

        cost += new_cost

        # print(f'tree_l : {tree_l}, cost : {cost}')
    if max_cost < cost:
        max_cost = cost

print(max_cost)