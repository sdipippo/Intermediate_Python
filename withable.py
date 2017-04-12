'''

Op, Fn, Keyword     Magic Method        Jargon
==============      =================   ===========
a + b               a.__add__(b)        addable
a / b               a.__div__(b)        divisible
print a             a.__str__()
>>> a               a.__repr__()
len(a)              a.__len__()         sizeable
a[b]                a.__getitem__(b)    indexable
with a:                                 context manager


'''

Class Foo:
    pass

with Foo():
    pass
