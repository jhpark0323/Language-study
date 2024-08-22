import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = [int(input()) for _ in range(n)]

maxTree = [0 for _ in range(4*n)]

def max_tree(idx, start, end):
    if start == end:
        maxTree[idx] = ls[start]
        return maxTree[idx]

    mid = (start + end) // 2
    left_val = max_tree(2*idx, start, mid)
    right_val = max_tree(2*idx+1, mid+1, end)
    maxTree[idx] = max(left_val, right_val)
    return maxTree[idx]

max_tree(1, 0, n-1)

minTree = [0 for _ in range(4*n)]

def min_tree(idx, start, end):
    if start == end:
        minTree[idx] = ls[start]
        return minTree[idx]

    mid = (start + end) // 2
    min_left_val = min_tree(2*idx, start, mid)
    min_right_val = min_tree(2*idx+1, mid+1, end)
    minTree[idx] = min(min_left_val, min_right_val)
    return minTree[idx]

min_tree(1, 0, n-1)

def find_tree(idx, start, end, left, right, tree, maxOrMin):
    if right < start or end < left:
        if maxOrMin == 1:
            return 0
        elif maxOrMin == 0:
            return 1e11

    if left <= start and end <= right:
        return tree[idx]

    mid = (start + end) // 2
    left_val = find_tree(2*idx, start, mid, left, right, tree, maxOrMin)
    right_val = find_tree(2*idx+1, mid+1, end, left, right, tree, maxOrMin)
    # 최댓값
    if maxOrMin == 1:
        return max(left_val, right_val)
    # 최솟값
    if maxOrMin == 0:
        return min(left_val, right_val)


for _ in range(m):
    a, b = map(int, input().split())
    print(find_tree(1, 0, n-1, a-1, b-1, minTree, 0), find_tree(1, 0, n-1, a-1, b-1, maxTree, 1))
