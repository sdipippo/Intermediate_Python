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
4) Class Method         Class.method()
    Implicitly passes the class object itself as the first argument
    Like passing in the "Tire" class when the Tire class calls the method
    Useful for alternate constructors

One problem with inheritance:
THe "Circle vs. Ellipse" problem
Which one should be the parent (base)?
If something is built into the base class that is not
appropriate for the child class, that is hard to deal with
No solution provided in class . . . other than not doing it.

Classes should pretty much always inherit from "Object" if not
inheriting from another class. It changes the "metaclass" to a newer
method

Open/Closed Principle
    Classes should be open for extension (inherit and override)
    and closed for modification (overrides have no side-effects

name mangling           self.method()
    prefixing your internal dependencies: __name
    mangles the name to:        _Class__name
    Meaning you would see it as _Class__name if you "dir" the class
    Prevents child classes from overwriting that dependency by mistake
    

'''

import math
from collections import namedtuple

Version = namedtuple('Version', 'major minor patch')

class Circle(object):
    'advanced circle analytics toolkit'

    #major, minor, patch
    version = Version(0, 6, 0)

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    # class method figures out which class is calling the method
    # Like, if Tire called it. Then it creates a "tire" class
    # instead of a Circle method
    #constructed for customer 5
    # who only creates circles based on
    # bounding box diagonal, not radius
    def from_bbd(cls, diagonal):
        'construct a new circle from a bounding box diagonal'
        radius = diagonal / math.sqrt(2)
        return cls(radius)

    # The 'property' built-in changes the behavior of the dot method
    # Used to retroactively insert getters and setters when you need them
    # The use of property requires us to pass in the Object arg
    @property
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    #radius = property(get_radius, set_radius)
        

    

    def __repr__(self):
        'Change how the name appears in IDLE'
        # We look at the metadata and fill in a class that inherits
        # this class, if there is one.
        return '%s(%r)' % (self.__class__.__name__,self.radius)

    def area(self):
        'Quadrature on a planar shape of uniform revolution'
        radius = self.__circumference() / math.pi / 2.0
        return math.pi * radius ** 2

    def circumference(self):
        'permeter of a circle'
        return math.pi * self.radius * 2

    # Creates a Circle-specific circumference value
    # So Tire can overwrite it in client code
    # and future changes could impact them
    __circumference = circumference
    # This creates 'name mangling' - see top documentation

    @staticmethod #This turns off the requirement to pass in "self"
    # Since the function doesn't need a Circle instance to run anyway
    # In reality, this method doesn't even really have to be in this class
    def angle_to_grade(angle):
        '''
        Convert an inclinometer reading in degrees to a percent-grade.
        '''
        return math.tan(math.radians(angle)) * 100.0

