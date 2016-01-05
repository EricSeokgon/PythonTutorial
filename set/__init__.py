__author__ = 'Hadeslee'

print set()
print set([1, 2, 3, 4, 5])
print set([1, 2, 3, 2, 3, 4])
print set('abc')
print set([(1, 2, 3), (4, 5, 6)])

A = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
print len(A)
print 5 in A
print 10 not in A

B = set([4, 5, 6, 10, 20, 30])
C = set([10, 20, 30])

print C.issubset(B)
print C <= B
print B.issuperset(C)
print B >= C
print
