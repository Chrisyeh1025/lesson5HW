student_score = list()
i = 1
print('請依序輸入五個人的成績')
while i < 6:
    score = int(input('請輸入成績'))
    student_score.append(score)
    i = i + 1
print('所有輸入的成績',student_score)
print('平均分數是:', sum(student_score)/len(student_score))
print('最高分數是:', max (student_score))
print('最低分數是:', min (student_score))


