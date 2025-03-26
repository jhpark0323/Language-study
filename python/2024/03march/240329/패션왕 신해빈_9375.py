from itertools import combinations

T = int(input())

for _ in range(T):
    n = int(input())

    dictionary = {}
    for i in range(n):
        a, b = input().split()
        if b not in dictionary.keys():
            dictionary[b] = [a]
        else:
            ls = dictionary[b]
            dictionary[b] = ls + [a]
    # print(dictionary)

    ans = 1
    for i in dictionary.values():
        # print(i)
        ans *= (len(i)+1)

    print(ans-1)