n = int(input())

ls = [0]*1001

ls[1] = 1
ls[2] = 2
for i in range(3, n+1):
    ls[i] = ls[i-1] + ls[i-2]
print(ls[n]%10007)