from collections import Counter

# Task 1: count the frequency of words in "Hamlet"
counts = Counter()
with open('C:\Users\sdipippo\Desktop\dialogue.txt') as f:
    for line in f:
        for word in line.split():
            counts[word] += 1

print counts.most_common(3)

# Task 2: Organize the unique words by first letter

words = {} #letter -- > set of words beginning with that letter

with open('C:\Users\sdipippo\Desktop\dialogue.txt') as f:
    for line in f:
        for word in line.split():
            initial = word[0]
            words.setdefault(initial, set()).add(word)
print words['v']

#alternate way to do task 2
from collections import defaultdict

words = defaultdict(set)

with open('C:\Users\sdipippo\Desktop\dialogue.txt') as f:
    for line in f:
        for word in line.split():
            initial = word[0]
            words[initial].add(word)
print words['v']

#Task 3: Organize the words
# chain     prev --> list of following words
# Every time you see a word, that's the key, and the value is the list of words
# following the word
#Example: If the key is "the", then the values are all words immediately following
# the word "the" in the document"
# the: castle, house, tower
import random

chain = defaultdict(list)
# Defaultdict always uses a default value if there is no existing key yet,
# as opposed to regular dictionary which would throw a key error
# In this case, it's saying that "Whenever you look up a key that
# doesn't exist, put an empty list into the value field"
last = None, None
with open('C:\Users\sdipippo\Desktop\dialogue.txt') as f:
    for line in f:
        for word in line.split():
            chain[last].append(word)
            last = (last[1], word)

capitalized = [word for word in chain if word[0] and word[0][0].isupper()]
last = random.choice(capitalized)
for word in last:
    print word,

while word[-1] not in '.?!':
    word = random.choice(chain[last])
    print word,
    last = (last[1], word)
