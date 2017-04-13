'''
The famous Fibonacci sequence: 0, 1, 1, 2, 3

each number is the sum of the two previous numbers

Profiling your code:
    - Can be in the CMD of Windows
    

'''

def nth(n):
    '''
    recursive version:
    
    the n-th term in the Fibonacci sequence.

        0-th: 0
        1-th: 1
        n-th: (n-1)th + (n-2)th
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    return nth(n-1) + nth(n-2)

def nth(n):
    'the iterative version'
    a,b = 0, 1
    for i in xrange(n):
        a, b = b, b + a
    return a

import decorators #module we wrote

@decorators.make_caching
def nth(n):
    '''
    recursive with memoization
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    return nth(n-1) + nth(n-2)


if __name__ == '__main__':
    import sys
    try:
        #sys.argv let's the user define # of tries (n) from the command line
        n = int(sys.argv[1])
    except (IndexError, ValueError):
        n = 100
    for i in range(n):
        print nth(i)
