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
print 
# the {} works by specifying a name:spcifier
# so we are specifying no name, but the '.2f' means
# "float to digits only", hence the answer generated was 1.09


# Customer 2: local rubber sheet company

cuts = [0.7, 0.3, 0.5]
circles = [Circle(radius) for radius in cuts]
for c in circles:
        print 'a circle with radius', c.radius
        print 'has a cold area {:.2f}'.format(c.area())
        print 'and a circumference {:.2f}'.format(c.circumference())
        c.radius *= 1.1
        print 'and a warm area {:.2f}'.format(c.area())
        print


# Customer 3: regional tire company

# class inheritance
class Tire(Circle):
    def circumference(self):
        'adjusted for width of tire'
        return Circle.circumference(self) * 1.25

'''
There are two types of methods
1) Bound method     instance.method()
    Regular instance method call
    implicitly passes the instance as first arg
2) unbound method   Class.method()
    regular method called from the class
    must explicitly pass the instance as first arg, as
    seen in Tire.circumference
Example:
    s = 'hello'
    s.upper() is a BOUND method
    str.upper(s) is UNBOUND. It doesn't know which
    instance from the class to use, so you are telling it
    which instance (usually "self")
'''


# a tire with 22 inch rim
t = Tire(22)
print 'A tire of radius', t.radius
print 'has an area {:.2f}'.format(t.area())
print 'and circumference {:.2f}'.format(t.circumference())
print


# Customer 4: National Trucking Company

print 'an incline of 7 degrees'
print 'is a {:.0f} grade'.format(Circle.angle_to_grade(7))
print

#Customer 5: International Graphics company
# We have money and power!
# We build circles NOT with radius,
# But with a bounding box diagonal
# r = d / sqrt(r) or d^2 = 2r^2

c = Circle.from_bbd(5)
print 'a circle with diagonal 5'
print 'has a radius {:.2f}'.format(c.radius)
print 'and an area {:.2f}'.format(c.area())
print



