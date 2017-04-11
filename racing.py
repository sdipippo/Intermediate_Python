'''
Let's explore race conditions!
1. The consumer might race ahead of the producer and early exit
    Solution: have consumer wait a bit before starting
    Better Solution: Use a Queue designed for coordinating threads (Queue module)
2. look-before-you-leap allows consumers to race against each other
    and accidentally pop from an empty deque.
    Solution: EAFP, use try/except instead
    Better Solution: Use a Queue designed for coordinating threads (Queue module)
3. Counting is a two-step process, get then set
    so, consumers can race against each other and create
    inconsistent counts
    Solution: lock the shared resource (counts) before using it
4. Main thread races against subthreads
    Our print statement was printing before subthreads were done
    Solution: wait until subthreads are done
'''

##################################################
#serial implementation to test against.

from collections import Counter
import re

counts = Counter()
with open('C:\Users\sdipippo\Desktop\dialogue.txt') as f:
    for line in f:
        for word in re.findall(r'[a-z]+',line.lower()):
            counts[word] +=1
print 'SERIAL'
print counts.most_common(3)

##################################################
#Parallel threads

from collections import deque #double-ended queue
from threading import Thread, Lock
import time
from Queue import Queue

counts = Counter()
counts_lock = Lock()
#pronounced "deck", like a deck of cards.
#Can pull cards from either end
q = Queue()

def producer(filename):
    with open(filename) as f:
        for line in f:
            for word in re.findall(r'[a-z]+',line.lower()):
                q.put(word)

def consumer():
    while True:
        word = q.get()
        with counts_lock: #acquire a lock
            current = counts[word]
            time.sleep(1e-5)
            counts[word] += 1
            #release lock
        q.task_done()

if __name__ == '__main__':
    filenames = ['C:\Users\sdipippo\Desktop\dialogue.txt']

    producers = [Thread(target=producer, args=(filename,)) for filename in filenames]
    for t in producers:
        t.start()

    consumers = [Thread(target=consumer) for i in range(2)]
    for t in consumers:
        t.daemon = True
        t.start()

    for t in producers:
        t.join() #wait for this thread to finish
    q.join()# wait until # of q.put == number of q.task_done
        
    print 'PARALLEL THREADS'
    print counts.most_common(3)
            
