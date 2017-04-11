'''Copyright (c) 2017 Circuitous, Inc.

Classes are for SHARED information
Instances are for UNIQUE information

Introspection
    Using code to learn about code (like gleaning
    the name of a class that inherited us)
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
