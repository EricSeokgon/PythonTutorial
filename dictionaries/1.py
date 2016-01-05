__author__ = 'Hadeslee'

member = {'basketball': 5, 'soccer': 11, 'baseball': 9}
member['volleybal'] = 7
print member
print

member['volleybal'] = 6
print member
print member['basketball']

del member['basketball']
print member

d = {}
d['str'] = 'abc'
print d

d[1] = 4
print d
d[(1, 2, 3)] = 'tuple'
print d

# d[[1, 2, 3]] = 10.0
# d[{1: 10}] = 10
