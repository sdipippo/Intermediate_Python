Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py 

Traceback (most recent call last):
  File "C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py", line 68, in <module>
    d['hero'] = 'Luke'
  File "C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py", line 59, in __setitem__
    if key in self:     # May create race condition, fix with better SQL
  File "C:\Python27\lib\_abcoll.py", line 388, in __contains__
    self[key]
  File "C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py", line 51, in __getitem__
    return json.loads(row[0])
TypeError: 'NoneType' object has no attribute '__getitem__'
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py 

Traceback (most recent call last):
  File "C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py", line 70, in <module>
    d['hero'] = 'Luke'
  File "C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py", line 61, in __setitem__
    if key in self:     # May create race condition, fix with better SQL
  File "C:\Python27\lib\_abcoll.py", line 388, in __contains__
    self[key]
  File "C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py", line 50, in __getitem__
    if row is None:
UnboundLocalError: local variable 'row' referenced before assignment
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py 
<__main__.SqlDict object at 0x0404D6D0>
<__main__.SqlDict object at 0x0404D6D0>
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py 
> c:\users\sdipippo\desktop\python programming\intermediate python ilt apr 2017\sqldict.py(45)__getitem__()
-> c = self.connection.cursor()
(Pdb) self
<__main__.SqlDict object at 0x0367D6D0>
(Pdb) key
'hero'
(Pdb) n
> c:\users\sdipippo\desktop\python programming\intermediate python ilt apr 2017\sqldict.py(50)__getitem__()
-> c.execute('SELECT value FROM Dict WHERE key=?', (key,))
(Pdb) p c
<sqlite3.Cursor object at 0x03721CE0>
(Pdb) help

Documented commands (type help <topic>):
========================================
EOF    bt         cont      enable  jump  pp       run      unt   
a      c          continue  exit    l     q        s        until 
alias  cl         d         h       list  quit     step     up    
args   clear      debug     help    n     r        tbreak   w     
b      commands   disable   ignore  next  restart  u        whatis
break  condition  down      j       p     return   unalias  where 

Miscellaneous help topics:
==========================
exec  pdb

Undocumented commands:
======================
retval  rv

(Pdb) help c
c(ont(inue))
Continue execution, only stop when a breakpoint is encountered.
(Pdb) c
> c:\users\sdipippo\desktop\python programming\intermediate python ilt apr 2017\sqldict.py(45)__getitem__()
-> c = self.connection.cursor()
(Pdb) q

Traceback (most recent call last):
  File "C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py", line 72, in <module>
    d['villain'] = 'Darth Vader'
  File "C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py", line 62, in __setitem__
    if key in self:     # May create race condition, fix with better SQL
  File "C:\Python27\lib\_abcoll.py", line 388, in __contains__
    self[key]
  File "C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py", line 45, in __getitem__
    c = self.connection.cursor()
  File "C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py", line 45, in __getitem__
    c = self.connection.cursor()
BdbQuit
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py 
> c:\users\sdipippo\desktop\python programming\intermediate python ilt apr 2017\sqldict.py(45)__getitem__()
-> c = self.connection.cursor()
(Pdb) q

Traceback (most recent call last):
  File "C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py", line 71, in <module>
    d['hero'] = 'Luke'
  File "C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py", line 62, in __setitem__
    if key in self:     # May create race condition, fix with better SQL
  File "C:\Python27\lib\_abcoll.py", line 388, in __contains__
    self[key]
  File "C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py", line 45, in __getitem__
    c = self.connection.cursor()
  File "C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py", line 45, in __getitem__
    c = self.connection.cursor()
BdbQuit
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py 
SqlDict('starwars.db', [(u'hero', u'Luke')])
SqlDict('starwars.db', [(u'hero', [u'Rey', u'Finn'])])
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py 
SqlDict('starwars.db', [(u'hero', u'Luke')])
SqlDict('starwars.db', [(u'hero', [u'Rey', u'Finn'])])
>>> SqlDict('starwars.db', [(u'hero', [u'Rey', u'Finn'])])

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    SqlDict('starwars.db', [(u'hero', [u'Rey', u'Finn'])])
TypeError: __init__() takes exactly 2 arguments (3 given)
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py 
SqlDict('starwars.db', [(u'hero', u'Luke')])
SqlDict('starwars.db', [(u'hero', [u'Rey', u'Finn'])])
>>> SqlDict('starwars.db', [(u'hero', [u'Rey', u'Finn'])])
SqlDict('starwars.db', [(u'hero', [u'Rey', u'Finn'])])
>>> d
SqlDict('starwars.db', [(u'hero', [u'Rey', u'Finn'])])
>>> del d['hero']
>>> d
SqlDict('starwars.db', [])
>>> del d['hero']
>>> d
SqlDict('starwars.db', [])
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py 
SqlDict('starwars.db', [(u'hero', u'Luke')])
SqlDict('starwars.db', [(u'hero', [u'Rey', u'Finn'])])
>>> len(d)
1
>>> del d['hero']
>>> len(d)
0
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 

Traceback (most recent call last):
  File "C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py", line 20, in <module>
    with Foo():
AttributeError: Foo instance has no attribute '__enter__'
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 

Traceback (most recent call last):
  File "C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py", line 24, in <module>
    pass
TypeError: __exit__() takes exactly 1 argument (4 given)
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 
(None, None, None)
>>> help(__exit__)

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    help(__exit__)
NameError: name '__exit__' is not defined
>>> f = Foo()
>>> help(f.__exit__)
Help on method __exit__ in module __main__:

__exit__(self, *args) method of __main__.Foo instance

>>> help(f.__enter__)
Help on method __enter__ in module __main__:

__enter__(self) method of __main__.Foo instance

>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 
entering the context
leaving the context
(None, None, None)
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 
entering the context
inside the context
leaving the context
(None, None, None)
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 

Traceback (most recent call last):
  File "C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py", line 30, in <module>
    with ContextManager():
TypeError: __init__() takes exactly 2 arguments (1 given)
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 
initializing the context manager
entering the context
inside the context
leaving the context
(None, None, None)
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 
initializing the context manager
entering the context
inside the context
leaving the context
(None, None, None)
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 
initializing the context manager
entering the context
inside the context
leaving the context
(None, None, None)
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 
initializing the context manager
entering the context
inside the context
None
last line of the context
leaving the context
(None, None, None)
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 
initializing the context manager
entering the context
inside the context
None
last line of the context
leaving the context
(None, None, None)
after the context
>>> x
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 
initializing the context manager
entering the context
inside the context
42
last line of the context
leaving the context
(None, None, None)
after the context
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 
initializing the context manager
entering the context
inside the context
42
leaving the context
(<type 'exceptions.RuntimeError'>, RuntimeError('oops',), <traceback object at 0x02F22EE0>)

Traceback (most recent call last):
  File "C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py", line 35, in <module>
    raise RuntimeError('oops')
RuntimeError: oops
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 
initializing the context manager
entering the context
inside the context
42
leaving the context
mark exception as handled
after the context
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 
initializing the context manager
entering the context
inside the context
42
leaving the context
mark exception as handled
after the context
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 
initializing the context manager
entering the context
inside the context
42
leaving the context
mark exception as handled
after the context
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 
initializing the context manager
entering the context
inside the context
42
last line of the context
leaving the context
after the context
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 

Traceback (most recent call last):
  File "C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py", line 50, in <module>
    with Suppress(OSError):
  File "C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py", line 42, in __init__
    self.etype
AttributeError: Suppress instance has no attribute 'etype'
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 
initializing the context manager
entering the context
inside the context
42
leaving the context
mark exception as handled
after the context
>>> 
>>> 
>>> tmp = sys.stdout

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tmp = sys.stdout
NameError: name 'sys' is not defined
>>> import sys
>>> tmp = sys.stdout
>>> sys.stdout = sys.stderr
>>> print 'red
SyntaxError: EOL while scanning string literal
>>> print 'red'
red
>>> sys.stdout = tmp
>>> print 'blue
SyntaxError: EOL while scanning string literal
>>> print 'blue'
blue
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\withable.py 
red
blue
initializing the context manager
entering the context
inside the context
42
leaving the context
mark exception as handled
after the context
>>> 
 RESTART: C:\Users\sdipippo\Desktop\Python Programming\Intermediate Python ILT Apr 2017\sqldict.py 
SqlDict('starwars.db', [(u'hero', u'Luke')])
SqlDict('starwars.db', [(u'hero', [u'Rey', u'Finn'])])
>>> 
