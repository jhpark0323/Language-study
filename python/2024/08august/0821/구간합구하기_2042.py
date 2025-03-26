import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = [0 for _ in range(4*n)]

def make_tree(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]

    mid = (start + end) // 2
    left_val = make_tree(start, mid, 2*idx)
    right_val = make_tree(mid+1, end, 2*idx+1)
    tree[idx] = left_val + right_val
    return tree[idx]

def update_tree(start, end, idx, target, value):
    if target < start or end < target:
        return

    tree[idx] += value
    if start == end:
        return

    mid = (start + end) // 2
    update_tree(start, mid, 2*idx, target, value)
    update_tree(mid+1, end, 2*idx+1, target, value)

def sum_tree(start, end, idx, left, right):
    if right < start or end < left:
        return 0

    if left <= start and right >= end:
        return tree[idx]

    mid = (start + end) // 2
    return sum_tree(start, mid, 2*idx, left, right) + sum_tree(mid+1, end, 2*idx+1, left, right)

make_tree(0, n-1, 1)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update_tree(0, n-1, 1, b-1, c-arr[b-1])
        arr[b-1] = c
    else:
        print(sum_tree(0, n-1, 1, b-1, c-1))