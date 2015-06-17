__author__ = 'sklee'
f = open("foo.txt",'w')
f.write("Life is too short, you need python")
f.close()

with open("foo.txt",'w') as f:
    f.write("Life is too short, you need python")