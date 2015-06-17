__author__ = 'sklee'
#첫 번째 줄을 읽어서 화면에 출력
f = open("새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

#모든 라인 읽어서 출력
f = open("새파일.txt", 'r')
while 1:
    line = f.readline()
    if not line: break
    print(line)
f.close()

#readlines() 이용하는 방법

f = open("새파일.txt", 'r')
lines = f.readlines()
for line in lines:
 print(line)
f.close()

#read()를 이용하는방법
f = open("새파일.txt",'r')
data = f.read()
print(data)
f.close()

#파일에 새로운 내용 추가하기

f = open("새파일.txt",'a')
for i in range(11,20):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()