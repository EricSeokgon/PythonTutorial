__author__ = 'Hadeslee'

D = {'a': 1, 'b': 2, 'c': 3}

for value in D.values():
    print value
print

items = D.items()
print items
print

items.sort()
print items
print

for k, v in items:
    print k, v
