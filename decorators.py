'''
Decorators

    @decorator
    def foo(...):
        ...

Identity Function
    the output is the same as the input

Higher-order function
    receives a function as input, and/or returns a function as output
    In add_docstring below, we take a function as input,
    edit the properties of that function, then return the function back

Pure Function
    1. Always returns the same output for a given input
    2. No side effects (only returns a value)

Wrapper Function
    uses another function (often called a 'helper')
    usually similar to, but improved

Factory Function
    a function that creates and returns a function

Closure (ex. pow2.__closure__[0].cell_contents will yield '2')
    A place to stash the local variables
    of the parent factory function for a child function defined
    inside of another function

**A decorator is just a function that receives another function**

'''

import math

### Factory Functions ##############

def pow2(base):
    return base ** 2

def pow3(base):
    return base ** 3

def make_pow(exponent):
    def power(base):
        return base ** exponent
    return power

powers = [make_pow(i) for i in range(100)]
# above makes 100 pow functions


### Wrapper Functions ##############

def logging_sin(x):
    print 'calling sin'
    print 'with', x
    result = math.sin(x)
    print 'result was', result
    return result

def logging_cos(x):
    print 'calling cos'
    print 'with', x
    result = math.cos(x)
    print 'result was', result
    return result

def make_logging(func):
    def logging_wrapper(x):
        print 'calling', func.__name__
        print 'with', x
        result = func(x)
        print 'result was', result
        return result
    logging_wrapper.__name__ = func.__name__
    logging_wrapper.__doc__ = func.__doc__
    return logging_wrapper



def better_sqrt(x):
    'sqrt that works on negative input'
    #1j represents imaginary number 'i'
    if x < 0:
        return math.sqrt(-x) * 1j
    return math.sqrt(x)

### Monkey Patching ###############
# You wouldn't do this if you had access to change the code "theirs"
# You would just change the code directly

import theirs

old_sqrt = math.sqrt

def patch_sqrt(x):
    if x < 0:
        return old_sqrt(-x) * 1j
    return old_sqrt(x)

math.sqrt = patch_sqrt


# Assume we cannot change code in "theirs".
# But we want to use negative numbers as input, and their
# code can't take that


print theirs.sqrts([4, 25, 16, 81])

#Higher-order functions##############

def identity(x):
    return x

registry = {}

def register(func):
    registry[func.__name__] = func
    return func

def add_docstring(func):
    if func.__doc__ is None:
        func.__doc__ = 'unknown documentation'
    return func

##### Regular Functions ##############
@make_logging
@add_docstring
@register
@identity
def square(x):
    'Multiply a number by itself'
    'square is a variable representing a function'
    return x ** 2

square = identity(square)
square = register(square)
square = add_docstring(square)

def power(base, exponent=2):
    return base ** exponent

power = register(power)
power = add_docstring(power)
power = make_logging(power)

@register #This is the SAME as the below code saying collatz = register(collatz)
@add_docstring
@make_logging
def collatz(x):
    'Half or Triple plus 1'
    if x % 2 == 0:
        return x // 2
    return 3 * x + 1

collatz = register(collatz)
collatz = add_docstring(collatz)
collatz = make_logging(collatz)

def conjecture(x):
    'Recursing collatz on itself will reach 1?'
    # Assume x >= 1 and integer
    if x == 1:
        return True
    x = collatz(x)
    return conjecture(x)
