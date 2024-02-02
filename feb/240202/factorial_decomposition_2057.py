import itertools

N = int(input())

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n-1)

# print(factorial(N))

# 0부터 N까지 순회를 하면서 factorial(i)가 N보다 커지면 멈추고 그 전까지 fac_ls에 append
fac_ls = []
for i in range(N):
    if factorial(i) > N:
        break
    # fac_ls.append(i)
    fac_ls.append(factorial(i))

# print(fac_ls)

# 부분집합을 전부다 구해주는 함수
def subset(ls):
    subset_ls = []
    # 다른 파일에 적어놨는데 부분집합 구하는 방법중에 하나인 combinations 사용함 -> 블랙잭에있음
    for i in range(1, len(ls)+1):
        subset_ls.extend(list(itertools.combinations(ls, i)))
    return subset_ls

subset_factorial = subset(fac_ls)
# print(subset_factorial)

# 각 부분집합의 합을 구해줘서 sum_subset에 append
sum_subset = []
for i in subset_factorial:
    sum_subset.append(sum(i))

# print(sum_subset)

if N in sum_subset:
    print('YES')
else:
    print('NO')