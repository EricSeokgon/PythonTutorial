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

