__author__ = 'Hadeslee'

f = lambda x: x + 1
print f(1)

g = lambda x, y: x + y
print g(1, 2)

incr = lambda x, inc=1: x + inc
print incr(10)
print incr(10, 5)

vargs = lambda x, *args: args
print vargs(1, 2, 3, 4, 5)
