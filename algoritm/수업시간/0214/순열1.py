def f(i, k):
    if i == k:
        print(*p)
    else:
        # p[i]자리에 올 원소 p[j]를 결정
        for j in range(i, k):
            # p[i] <-> p[j]
            p[i], p[j] = p[j], p[i]
            f(i+1, k)
            # p[i] <-> p[j] (원상복구)
            p[i], p[j] = p[j], p[i]

n = 3
p = [1, 2, 3]

f(0, n)