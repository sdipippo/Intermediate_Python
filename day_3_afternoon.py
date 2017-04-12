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
