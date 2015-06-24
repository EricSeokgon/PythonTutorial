__author__ = 'sklee'
try:
    f = open('foo.txt''r')
except FileNotFoundError as e:
    print(e)
else:
    data = f.read()
    f.close()
