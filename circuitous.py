'''Copyright (c) 2017 Circuitous, Inc.


'''

class Circle:
    'advanced circle analytics toolkit'

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        'Quadrature on a planar shape of uniform revolution'
        return 3.14159 * self.radius ** 2

    def circumference(self):
        'permeter of a circle'
        return 3.14 * self.radius * 2
