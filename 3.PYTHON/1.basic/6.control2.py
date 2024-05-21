x = 10

if x < 10:
    print('x가 10보다 작습니다')
else:
    print('x가 10보다 큽니다')

#--------------------------------------

score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(score, grade)

print("Score: {}, Grade: {}".format(score, grade))

print("Score: {1}, Grade: {0}".format(grade, score))

print( '점수는 {score} 이고, 성적은 {grade} 입니다 ')  # 문자열
print(f'점수는 {score} 이고, 성적은 {grade} 입니다 ')  #포맷팅

math = 90
eng = 80

if math >= 90 and eng >= 90:
    print('졸업조건 충족\t안녕히가세요')
else:
    print('졸업 미흡\n힘내세요')
