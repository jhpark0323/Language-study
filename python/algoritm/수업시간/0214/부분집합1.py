# k개의 원소를 가진 배열a에서 부분집합의 합이 t인 경우
def f(i, k, s, t):
    global cnt
    cnt += 1
    # 모든 원소에 대해 결정 하면
    if s == t:
        for j in range(k):
            # a[j]가 포함된 경우
            if bit[j]:
                print(a[j], end = ' ')
        print()
    # 모든 원소를 고려했으나 s!=t
    elif i == k:
        return
    # 고려한 원소의 합이 t보다 큰경우
    elif s > t:
        return

    else:
        # for j in range(1, -1, -1):
        #     bit[i] = j
        #     f(i+1, k, t)
        bit[i] = 1
        f(i+1, k, s+a[i], t)
        bit[i] = 0
        f(i + 1, k, s, t)

n = 10
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# bit[i]는 a[i]가 부분집합에 포함되는지 표시
bit = [0] * n
cnt = 0
f(0, n, 0, 1)
print('cnt : ',cnt)