import sys
input = sys.stdin.readline
n = int(input())
an = list(map(int, input().split()))
bn = list(map(int, input().split()))
m = int(input())
cn = list(map(int, input().split()))

def qstack(element):
    for i in range(n):
        # stack일 때는 그냥 넘어가도 됨
        # q 일때
        if not an[i]:
            element, bn[i] = bn[i], element

    return element

for insert in cn:
    print(qstack(insert), end=' ')
