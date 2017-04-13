'''

Op, Fn, Keyword     Magic Method            Jargon
==============      =================       ===========
a + b               a.__add__(b)            addable
a / b               a.__div__(b)            divisible
print a             a.__str__()
>>> a               a.__repr__()
len(a)              a.__len__()             sizeable
a[b]                a.__getitem__(b)        indexable
with a:             __enter__, __exit__     context manager

If it's always the same beginning and end, but the middle is different,
that's a "with" block
'''

class ContextManager:
    'a generic context manager, basically a "with"'

    def __init__(self, value):
        print 'initializing the context manager'
        self.value = value

    def __enter__(self):
        print 'entering the context'
        return self.value #hand this value to 'with . . . as . . . '
    
    def __exit__(self, etype, einstance, etraceback):
        #Exit takes 3 args
        #1. Exception Type
        #2. Exception itself
        #3. Exception traceback
        print 'leaving the context'
        if etype is not None and issubclass(etype, RuntimeError):
            print 'mark exception as handled'
            return True #returning True makes the program think it has been handled


class Suppress:
    'ignore some errors'
    def __init__(self, etype):
        self.etype = etype
    def __enter__(self):
        return self
    def __exit__(self, etype, e, tb):
        if etype and issubclass(etype, self.etype):
            return True

class Closing:
    'close the object upon leaving the context'
    def __init__(self, closeable):
        self.obj = closeable
    def __enter__(self):
        return self.obj
    def __exit__(self, *args):
        self.obj.close()

class RedirectStdout:
    'swap stdout to some other stream'

    def __init__(self, target_stream):
        self.target = target_stream

    def __enter__(self):
        self.old_stdout = sys.stdout
        sys.stdout = self.target
        return self

    def __exit__(self, *args):
        sys.stdout = self.old_stdout

import os, sys

with RedirectStdout(sys.stderr):
    print 'red'
print 'blue'

with Suppress(OSError):
    os.remove('tmp.txt')

with ContextManager(42) as x:
    print 'inside the context'
    print x
    raise RuntimeError('oops')
    print 'last line of the context' # never runs when above exception hits,
    # even if exception is handled

print 'after the context'
