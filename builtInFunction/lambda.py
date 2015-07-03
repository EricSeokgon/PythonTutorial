__author__ = 'hadeslee'
sum = lambda a, b : a+b
print(sum(3,4))

l = [lambda a,b:a+b, lambda a,b:a*b]
print(l)
print(l[0])
print(l[0](3,4))
print(l[1](3,4))