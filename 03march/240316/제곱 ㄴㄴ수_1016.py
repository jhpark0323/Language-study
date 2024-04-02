import math

min_val, max_val = map(int, input().split())

def f():
    num = [True] * (max_val-min_val+1)

    for i in range(2, int(math.sqrt(max_val))+1):
        # print(i)
        start = i ** 2
        if start < min_val:
            start = ((min_val - 1) // start + 1) * start

        for j in range(start, max_val+1, i**2):
            num[j-min_val] = False

    # print(num)

    # for i in range(len(num)):
    #     if num[i]:
    #         print(i+min_val)

    return sum(num)

cnt = f()
print(cnt)