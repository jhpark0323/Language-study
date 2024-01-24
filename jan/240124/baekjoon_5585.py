n = int(input())
n = 1000 - n
changes_ls = [500, 100, 50, 10, 5, 1]
changes = 0
i = 0

while True:
    if n >= changes_ls[i]:
        changes += n // changes_ls[i]
        n %= (changes_ls[i])
    i += 1

    if n == 0:
        break

print(changes)