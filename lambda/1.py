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


def f1(x):
    return x * x + 3 * x - 10


def f2(x):
    return x * x * x


def g(func):
    return [func(x) for x in range(-10, 10)]


print g(f1)
print g(f2)


def g(func):
    return [func(x) for x in range(-10, 10)]


print g(lambda x: x * x + 3 * x - 10)
print g(lambda x: x * x * x)


def f(x):
    return x * x


X = [1, 2, 3, 4, 5]
Y = map(f, X)
print Y


def f(x):
    return x * x


X = [1, 2, 3, 4, 5]
Y = []
for x in X:
    y = f(x)
    Y.append(y)
print Y

X = [1, 2, 3, 4, 5]
print map(lambda x: x * x, X)

y = map(lambda x: len(x), ['Hello', 'Python', 'Promramming'])
print y

print filter(lambda x: x > 2, [1, 2, 3, 34])

print filter(lambda x: x % 2 - 1, [1, 2, 3, 4, 5, 6])


def F():
    x = 1
    print filter(lambda a: a > x, range(-5, 5))


F()

print filter(lambda x: x > 2, [1, 2, 3, 34])
print filter(lambda x: x > 2, (1, 2, 3, 34))
print filter(lambda x: x < 'a', 'abcABCdefDEF')

print reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 100)
print reduce(lambda x, y: x + y * y, range(1, 11), 0)
x = 0
for y in range(1, 11):
    x = x + y * y
print x

