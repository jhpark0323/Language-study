def b(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

n = int(input())
ls_n = list(map(int, input().split()))

m = int(input())
ls_m = list(map(int, input().split()))

ls_n.sort()

for i in ls_m:
    print(b(ls_n, i))