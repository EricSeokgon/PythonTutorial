__author__ = 'Hadeslee'

phone = {'jack': 12312, 'jin': 1111, 'joseph': 2555667}
p = phone

print phone.keys()
print phone.values()
print phone.items()
print
print 'jack' in phone
print 'lee' in phone

phone['jack'] = 1234
print phone
print p
print

ph = phone.copy()
phone['jack'] = 111
print phone
print ph
