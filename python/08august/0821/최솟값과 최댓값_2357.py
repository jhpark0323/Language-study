n, m = map(int, input().split())
ls = [int(input()) for _ in range(n)]

tree = [0 for _ in range(4*n)]

def max_tree(idx, start, end):
    if start == end:
        tree[idx] = ls[start]
        return tree[idx]

    mid = (start + end) // 2
    left_val = max_tree(2*idx, start, mid)
    right_val = max_tree(2*idx+1, mid+1, end)
    tree[idx] = left_val + right_val
    return tree[idx]

max_tree(1, 0, n-1)
print(tree)