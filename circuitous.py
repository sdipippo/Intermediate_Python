'''Copyright (c) 2017 Circuitous, Inc.


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
        return 'Circle(%r)' % self.radius

    def area(self):
        'Quadrature on a planar shape of uniform revolution'
        return math.pi * self.radius ** 2

    def circumference(self):
        'permeter of a circle'
        return math.pi * self.radius * 2
