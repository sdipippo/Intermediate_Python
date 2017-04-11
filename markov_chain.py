'''
Markov Chain Monte Carlo
random sentence generator
'''

from collections import defaultdict
import random

def chain_init(filename, size=1):
    chain = defaultdict(list)
    last = (None,) * size
    with open(filename) as f:
        for line in f:
            for word in line.split():
                chain[last].append(word)
                last = last[1:] + (word,)
    return chain

def chain_walk(chain):
    last = random.choice(list(chain))
    for word in last:
        print word,
    while word[-1] not in '.?!':
        word = random.choice(chain[last])
        print word,
        last = last[1:] + (word,)

#Below code says "If run locally, execute code". If imported,
#don't run automatically. Wait to be invoked.
if __name__ == '__main__':
    chain = chain_init('data/dialogue.txt')
    chain_walk(chain)
