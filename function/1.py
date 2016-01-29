__author__ = 'sklee'


def sum(a, b):
    return a + b


a = 3
b = 4
c = sum(a, b)
print(c)


def sum2(a, b):
    result = a + b
    return result


a = sum2(3, 5)
print(a)


def say():
    return 'HI'


a = say()
print(a)


def sum2(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))


a = 5
b = 5
c = sum2(a, b)

