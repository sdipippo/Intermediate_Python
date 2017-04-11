'''
Our customers' code.
'''

from circuitous import Circle
from random import random,seed

# Customer 1: Our academic friends.

print 'Proposal to research the areas of circles'
print 'using Circuitous(tm)', Circle.version
n = 1000
seed(42)
#circles = [Circle(random()) for i in range(n)]
#areas = [circle.area() for circle in circles]
#use generator instead
circles = (Circle(random()) for i in xrange(n))
areas = (circle.area() for circle in circles)

print 'The average area of', n, 'random circles'
print 'seeded on the Answer to Life, and Everything'
print 'is {:.2f}'.format(sum(areas) / n)
# the {} works by specifying a name:spcifier
# so we are specifying no name, but the '.2f' means
# "float to digits only", hence the answer generated was 1.09

