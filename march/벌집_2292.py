n = int(input())

i = 0
floor = 1
while 1:
    floor += 6*i

    if n <= floor:
        print(i+1)
        break

    i += 1