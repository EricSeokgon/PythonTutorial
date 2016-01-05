__author__ = 'Hadeslee'

t = (12345, 54321, 'hello!')
u = t, (1, 2, 3, 4, 5)
print u

t2 = [1, 2, 3]
u2 = t2, (1, 2, 4)
print u2

t3 = {1: "abc", 2: "def"}
u3 = t3, (1, 2, 3)
print u3

t1 = ()
t2 = (1, 2, 3,)
t3 = 1, 2, 3
print type(t1), type(t2), type(t3)
