__author__ = 'sklee'
#for 알아보기
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
#학생 성적 검사
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격 입니다." %number)
    else:
        print("%d번 학생은 불합격 입니다." %number)

#for와 continue
marks = [90, 25, 67, 45, 80, 50]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." %number)