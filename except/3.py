__author__ = 'sklee'
f = open('foo.txt','w')
try:
    1*1
finally:
    f.close()
