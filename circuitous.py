'''Copyright (c) 2017 Circuitous, Inc.

Classes are for SHARED information
Instances are for UNIQUE information

Introspection
    Using code to learn about code (like gleaning
    the name of a class that inherited us)

Method Types:
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
3) Static method       Class.method()
    Function that belongs to a class
    Does not use an instance of that class at all
    Could be moved outside of a class and still work
    Therefore no need for "self"
    Sometimes people "just expect" their tools / functions
    to be in the same place as other tools. This is the use-case
    for this method type
'''

import math
from collections import namedtuple

Version = namedtuple('Version', 'major minor patch')

class Circle:
    'advanced circle analytics toolkit'

    #major, minor, patch
    version = Version(0, 1, 0)

    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        'Change how the name appears in IDLE'
        # We look at the metadata and fill in a class that inherits
        # this class, if there is one.
        return '%s(%r)' % (self.__class__.__name__,self.radius)

    def area(self):
        'Quadrature on a planar shape of uniform revolution'
        return math.pi * self.radius ** 2

    def circumference(self):
        'permeter of a circle'
        return math.pi * self.radius * 2

    @staticmethod #This turns off the requirement to pass in "self"
    # Since the function doesn't need a Circle instance to run anyway
    # In reality, this method doesn't even really have to be in this class
    def angle_to_grade(angle):
        '''
        Convert an inclinometer reading in degrees to a percent-grade.
        '''
        return math.tan(math.radians(angle)) * 100.0

