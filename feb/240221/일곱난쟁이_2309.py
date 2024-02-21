real = []

for _ in range(9):
    height = list(map(int, input().split()))
    real.extend(height)

# print(real)
total_sum = sum(real)
# print(total_sum)
# print(type(total_sum))

for i in range(9):
  for j in range(9):
    if i != j:
      current_sum = total_sum - real[i] - real[j]
      if current_sum == 100:
        rm1, rm2 = real[i], real[j]
        real.remove(rm1)
        real.remove(rm2)
        break
  if len(real) == 7:
    break

real.sort()

for i in real:
  print(i)
