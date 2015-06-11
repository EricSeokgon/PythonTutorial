__author__ = 'sklee'
odd = [1,3,5,7,9]
print(odd)
print(odd[0])
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3])

a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])

#리스트를 더하고(+) 반복하기(*)
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

a = [1, 2, 3]
print(a*3)

#리스트의 수정 변경과 삭제
a = [1, 2, 3]
a[2] = 4
print(a)

#리스트 수정
a[1:2] =['a', 'b', 'c']
print(a)

#리스트 요소 삭제
a[1:3]=[]
print(a)

#리스트 요소 삭제 2

del a[1]
print(a)
