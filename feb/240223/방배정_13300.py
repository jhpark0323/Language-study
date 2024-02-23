import math
std = []

N, K = map(int, input().split())

for i in range(N):
    s, y= map(int, input().split())
    std.append([s, y])

std.sort()

std_set = list(map(list, set(map(tuple, std))))
room = 0

for i in range(len(std_set)):
    room += math.ceil(std.count(std_set[i]) / K)
print(room)