# Task 1: count the frequency of words in "Hamlet"
counts = {}
with open('C:\Users\sdipippo\Desktop\dialogue.txt') as f:
    #Create a generator to read the file
    for line in f:
        for word in line.split():
            counts[word] = counts.get(word, 0) + 1
            # the .get method looked for the key in the dictionary.
            # If it's not there, add it with a value of 0
            
#Task 1a: Show the top 3 most frequent words
### print sorted(counts.items(), reverse=True)[:3]
# The problem with the above line is that it sorts on keys, not values
# We need to tell Python to use the value instead for sorting
def keyfunc(pair):
    return pair[1]

print sorted(counts.items(), key=keyfunc, reverse=True)[:3]
# the key parameter of sorted lets us pass in which "thing to sort by"

# We could have also used lambda instead of a function
# Lambda means "make a function"
print sorted(counts.items(), key=lambda pair: pair[1], reverse=True)[:3]
