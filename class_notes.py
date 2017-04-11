Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
# 4 basic types
>>> #4 basic collections
>>> 
>>> str, float, int, bool
(<type 'str'>, <type 'float'>, <type 'int'>, <type 'bool'>)
>>> list, dict, tuple, set
(<type 'list'>, <type 'dict'>, <type 'tuple'>, <type 'set'>)
>>> 

>>> 
>>> names = ['John', 'Paul', 'George', 'Ringo']
>>> for name in names:
	print name

	
John
Paul
George
Ringo
>>> 
>>> for name in reversed(names):
	print name

	
Ringo
George
Paul
John
>>> for name in names.reverse:
	print name

	

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    for name in names.reverse:
TypeError: 'builtin_function_or_method' object is not iterable
>>> for name in names.reverse():
	print name

	

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    for name in names.reverse():
TypeError: 'NoneType' object is not iterable
>>> 
>>> names[:]
['Ringo', 'George', 'Paul', 'John']
>>> names[::-1]
['John', 'Paul', 'George', 'Ringo']
>>> reversed(names)
<listreverseiterator object at 0x0373DBD0>
>>> 
>>> 
>>> 
>>> names = ['John', 'Paul', 'George', 'Ringo']
>>> for i, name in enumerate(names):
	print i, name

	
0 John
1 Paul
2 George
3 Ringo
>>> 
>>> 
>>> sorted(names)
['George', 'John', 'Paul', 'Ringo']
>>> names.sort()
>>> 
>>> 
>>> names
['George', 'John', 'Paul', 'Ringo']
>>> 
>>> #cntrl p and alt p cycle through shell history
>>> roles = ['guitar', 'bass', 'guitar', 'drums']
>>> for name, role in zip(names, roles):
	print name, role

	
George guitar
John bass
Paul guitar
Ringo drums
>>> help(zip)
Help on built-in function zip in module __builtin__:

zip(...)
    zip(seq1 [, seq2 [...]]) -> [(seq1[0], seq2[0] ...), (...)]
    
    Return a list of tuples, where each tuple contains the i-th element
    from each of the argument sequences.  The returned list is truncated
    in length to the length of the shortest argument sequence.

>>> 
>>> map(len, names)
[6, 4, 4, 5]
>>> 
>>> help(map)
Help on built-in function map in module __builtin__:

map(...)
    map(function, sequence[, sequence, ...]) -> list
    
    Return a list of the results of applying the function to the items of
    the argument sequence(s).  If more than one sequence is given, the
    function is called with an argument list consisting of the corresponding
    item of each sequence, substituting None for missing values when not all
    sequences have the same length.  If the function is None, return a list of
    the items of the sequence (or a list of tuples if more than one sequence).

>>> name[0] for name in names]
SyntaxError: invalid syntax
>>> [name[0] for name in names]
['G', 'J', 'P', 'R']
>>> 
>>> 
>>> a = [10, 20]
>>> a
[10, 20]
>>> a.append([30, 40])
>>> len(a)
3
>>> a
[10, 20, [30, 40]]
>>> b = a
>>> a == b
True
>>> a[0] = 'changed'
>>> a
['changed', 20, [30, 40]]
>>> b
['changed', 20, [30, 40]]
>>> 

>>> a = [10, 20]
>>> a.append([30, 40])
>>> b = list(a)
>>> b
[10, 20, [30, 40]]
>>> a
[10, 20, [30, 40]]
>>>  == b
 
  File "<pyshell#69>", line 2
    == b
    ^
IndentationError: unexpected indent
>>> a == b
True
>>> a is b
False
>>> 
>>> 
>>> b = a[:]
>>> a == b
True
>>> a is b
False
>>> # same result as the list function but more pythonic
>>> # Dictionaries have a .copy function
>>> dict.copy
<method 'copy' of 'dict' objects>
>>> 
>>> 
>>> 
>>> a[0] = 'changed'
>>> a
['changed', 20, [30, 40]]
>>> b
[10, 20, [30, 40]]
>>> 
>>> a[2]
[30, 40]
>>> a[2][0] = 'also changed'
>>> a
['changed', 20, ['also changed', 40]]
>>> b
[10, 20, ['also changed', 40]]
>>> 
>>> #shallow copy
>>> # make a copy, but only the 'first layer'
>>> a = [10, 20, [30, 40]]
>>> import copy
>>> b = copy.deepcopy(a)
>>> #deep copy - recursively make copies of every nested structure
>>> a[2][0] = 'changed'
>>> a
[10, 20, ['changed', 40]]
>>> b
[10, 20, [30, 40]]
>>> 
>>> 
>>> 
>>> #list comprehension
>>> stuff = []
>>> for record in rows:
	selection = record[1:]
	stuff.append(selection)

	

Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    for record in rows:
NameError: name 'rows' is not defined
>>> rows = [[10, 20, 30], [21, 22, 23], [35, 36]]
>>> for record in rows:
	selection = record[1:]
	stuff.append(selection)

	
>>> stuff
[[20, 30], [22, 23], [36]]
>>> #To use list comprehension, do it this way
>>> stuff = record[1:] for record in rows]
SyntaxError: invalid syntax
>>> stuff = [record[1:] for record in rows]
>>> 
>>> stuff
[[20, 30], [22, 23], [36]]
>>> 
>>> 
>>> [x ** 2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> names = ['John', 'Paul', 'George', 'Ringo']
>>> names{:]
SyntaxError: invalid syntax
>>> names[:]
['John', 'Paul', 'George', 'Ringo']
>>> names[:2]
['John', 'Paul']
>>> names[:2] = [0,1]
>>> names
[0, 1, 'George', 'Ringo']
>>> del names[1:2]
>>> names
[0, 'George', 'Ringo']
>>> 
>>> 
>>> names[:] = [1, 2, 3]
>>> names
[1, 2, 3]
>>> 
>>> names = [1, 2, 3]
>>> name

Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> names
[1, 2, 3]
>>> 
>>> # Using the above slice method to re-assign the list values preserved the same memory location of the list
>>> # As opposed to the method below that using [] which reassigns new memory
>>> 
>>> names = ['John', 'Paul', 'George', 'Ringo']
>>> for i in range(len(names)):
	print names[:i]

	
[]
['John']
['John', 'Paul']
['John', 'Paul', 'George']
>>> names[:-4]
[]
>>> names[:-3]
['John']
>>> for i in range(len(names)):
	print names[:-i]

	
[]
['John', 'Paul', 'George']
['John', 'Paul']
['John']
>>> # a negative index in a slice
>>> #on the right hand can NEVER get the whole list
>>> # on the left hand can NEVER get an empty list
>>> 
>>> -0
0
>>> 
>>> # imagine some 4-bit signed 2's complement integers
>>> 
>>> # decimal
>>> # decimal                     binary
>>> 0                             0 000
SyntaxError: invalid syntax
>>> #1                            0 001
>>> #...
>>> #7                            0 111
>>> #-8                           1 000
>>> 
>>> 
>>> 
>>> 1 / 3
0
>>> float(1/3)
0.0
>>> 5 / 3
1
>>> 1.0 / 3.0
0.3333333333333333
>>> 
>>> from __future__ import division
>>> 5 / 3
1.6666666666666667
>>> 1 / 3
0.3333333333333333
>>> 5 // 3
1
>>> # You should use // for integers divided by integers if you expect an integer returned
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 5.0 + 0.75
5.75
>>> 5.5 + 1.1
6.6
>>> 2.2 + 1.1
3.3000000000000003
>>> # IEEE 754: 64-bit floating point
>>> # 3.3 is tricky to store in 64-bits in binary
>>> 
>>> 
>>> 
>>> a = 2.2 + 1.1
>>> b = 3.3
>>> a == b
False
>>> #Floating point tends to be slightly inaccurate
>>> # So sometimes you just want to know if they are really close to each other
>>> 
>>> epsilon = 1e-9
>>> abs(a - b) < epsilon
True
>>> # Epsilon is the difference allowed to still prove true
>>> 
>>> def is_close(a, b, epsilon=-1e9):
	return abs(a - b) < epsilon

>>> is_close(a, b)
False
>>> def is_close(a, b, epsilon=1e-9):
	return abs(a - b) < epsilon

>>> is_close(a,b)
True
>>> 

>>> 
>>> # What if we do care about accuracy?
>>> from decimal import Decimal
>>> Decimal('0.1')
Decimal('0.1')
>>> # Infinite precision decimals
>>> [Decimal('0.1')] * 10
[Decimal('0.1'), Decimal('0.1'), Decimal('0.1'), Decimal('0.1'), Decimal('0.1'), Decimal('0.1'), Decimal('0.1'), Decimal('0.1'), Decimal('0.1'), Decimal('0.1')]
>>> sum([Decimal('0.1')] * 10)
Decimal('1.0')
>>> # But it is still not perfect
>>> 
>>> 


>>> 
>>> from fractions import Fraction
>>> Fraction(1,3)
Fraction(1, 3)
>>> Fraction(1,3) + Fraction(2,3)
Fraction(1, 1)
>>> 
>>> 
>>> 
>>> 
>>> 
