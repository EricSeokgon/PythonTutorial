def ismutable(obj):
    result = True
    com = obj.__class__.__name__
    if com not in ['int', 'float', 'str', 'tuple']:
        result = False
    return (com, result)


print 'str is ', ismutable('a')
print 'list is', ismutable([])
print 'tuple is', ismutable((1,))
print 'dict is', ismutable({})
print 'object is', ismutable(object)
print 'function is', ismutable(lambda x: x)
