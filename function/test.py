__author__ = 'Hadeslee'


def f5(b):
    b['a'] = 10
    a = {"a": 1, "b": 2}
    f5(a)
    print a


def print_menu():
    print '1. Snack'
    print '2. Snack'
    print '3. Snack'
    return


a = print_menu()
print a


def swap(x, y):
    return y, x


a = 10
b = 20
print a, b
print

a, b = swap(a, b)
print a, b
print


def add(a, b):
    return a + b


c = add(1, 3.4)
d = add('abc', 'typing')
e = add(['list'], ['and', 'list'])
print a
print b
print c


def incr(a, step=1):
    return a + step


b = 1
b = incr(b)
print b
b = incr(b, 10)
print b
