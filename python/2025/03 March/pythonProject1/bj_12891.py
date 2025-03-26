s, p = map(int, input().split())
dna = input()
a, c, g, t = map(int, input().split())

ans = 0
ls = [0] * 4

# 처음 p개 확인
for i in range(p):
    if dna[i] == "A":
        ls[0] += 1
    elif dna[i] == "C":
        ls[1] += 1
    elif dna[i] == "G":
        ls[2] += 1
    elif dna[i] == "T":
        ls[3] += 1

if a <= ls[0] and c <= ls[1] and g <= ls[2] and t <= ls[3]:
    ans += 1

for i in range(s - p):
    if dna[i] == "A":
        ls[0] -= 1
    elif dna[i] == "C":
        ls[1] -= 1
    elif dna[i] == "G":
        ls[2] -= 1
    elif dna[i] == "T":
        ls[3] -= 1

    if dna[i+p] == "A":
        ls[0] += 1
    elif dna[i+p] == "C":
        ls[1] += 1
    elif dna[i+p] == "G":
        ls[2] += 1
    elif dna[i+p] == "T":
        ls[3] += 1

    if a <= ls[0] and c <= ls[1] and g <= ls[2] and t <= ls[3]:
        ans += 1

print(ans)