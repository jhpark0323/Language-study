import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
ls = [int(input()) for _ in range(n)]
tree = [0 for _ in range(4*n)]

def make_tree(idx, start, end):
    if start == end:
        tree[idx] = ls[start]
        return tree[idx]

    mid = (start + end) // 2
    left_value = make_tree(2*idx, start, mid)
    right_value = make_tree(2*idx+1, mid+1, end)
    tree[idx] = left_value * right_value % 1000000007
    return tree[idx]

def update_tree(idx, start, end, target, value):
    if target < start or end < target:
        return

    if start == end:
        tree[idx] = value
    else:
        mid = (start + end) // 2
        update_tree(2*idx, start, mid, target, value)
        update_tree(2*idx+1, mid+1, end, target, value)
        tree[idx] = tree[2*idx] * tree[2*idx+1] % 1000000007

def cal_tree(idx, start, end, left, right):
    if right < start or end < left:
        return 1

    if left <= start and end <= right:
        return tree[idx]

    mid = (start + end) // 2
    left_value = cal_tree(2*idx, start, mid, left, right)
    right_value = cal_tree(2*idx+1, mid+1, end, left, right)
    return left_value * right_value % 1000000007

make_tree(1, 0, n-1)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update_tree(1, 0, n-1, b-1, c)
    else:
        print(cal_tree(1, 0, n-1, b-1, c-1))