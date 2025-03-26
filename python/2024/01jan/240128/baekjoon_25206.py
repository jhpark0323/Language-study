score = []
for _ in range(20):
    score.append(list(input().split()))
# print(score)

score_dict = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0
    }

new_score = []

for i in range(len(score)):
    if score[i][2] != 'P':
        score[i][2] = score_dict[score[i][2]]
        score[i][1] = float(score[i][1])
        new_score.append(score[i])

# print(score)

major_sum = 0
total_grade = 0
for i in range(len(new_score)):
    major_sum += new_score[i][1] * new_score[i][2]
    total_grade += new_score[i][1]


major_rate = major_sum / total_grade
print(major_rate)