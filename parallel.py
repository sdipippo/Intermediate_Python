'''
Parallel threads and processes the easy way!

The GIL (Global Interpreter Lock) prevents the CPython
Interpreter from doing compute on parallel threads

Going around the GIL
    - use processes
    - don't use CPython
    - use NumPy . . . probably most popular
    - use Cython
'''
import time, random
from multiprocessing.pool import ThreadPool #undocumented module
from multiprocessing import Pool #is documented

def io_bound(x):
    'simulate an input/output constrained task'
    time.sleep(random.uniform(0, 2))
    return x + 1

def cpu_bound(x):
    'compute-constrained tas'
    sum(xrange(int(1e8)))
    return x + 1

def serial(func, n):
    start = time.time()
    for result in map(func, xrange(n)):
        print result
    stop = time.time()
    print 'DURATION {:.2f}'.format(stop - start)

def threaded(func, n, maxthreads=25):
    'This module allows us to use multiple threads to accomplish the task'
    start = time.time()
    pool = ThreadPool(min(n, maxthreads)) # Create a number of threads (n)
    for result in pool.imap(func, xrange(n)):
        print result
    stop = time.time()
    print 'DURATION {:.2f}'.format(stop - start)

if __name__ == '__main__':
    serial(io_bound, 10)
    threaded(io_bound, 10) #Run the task with 10 threads
    serial(cpu_bound, 25)
