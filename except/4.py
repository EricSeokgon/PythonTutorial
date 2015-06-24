__author__ = 'sklee'
try:
    f = open("나없는파일",'r')
except FileNotFoundError:
    pass
