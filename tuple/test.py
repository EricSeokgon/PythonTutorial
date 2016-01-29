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

t = (1, 2, 3)
print t * 2
print t + ('PyKUG', 'users')
print t
print

print t[0], t[1:3]
print len(t)
print 1 in t

x, y, z = (1, 2, 3)
print type(x), type(y), type(z)
print x
print y
print z
print

x = 1
y = 2
x, y = y, x
print x, y


def calc(a, b):
    return a + b, a * b


x, y = calc(4, 5)
print x
print y

print 'id : %s, name : %s' % ('sklee', 'seok gon')

d = {'one:': 1, 'two': 2}
print d.items()
