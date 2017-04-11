'''
All about properties

Problem with the base code is that if we manually update
p.low or p.high after creation, p.mid doesn't update with it
So we can't have mid in init. Have to change it to it's own place / function


'''
from __future__ import division

class PriceRange(object):

    def __init__(self, low, high):
        self.low = low
        self.high = high

    @property
    def high(self):
        return self._high

    @high.setter
    def high(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('expected a number')
        if value < 0:
            raise ValueError('must be positive')
        self._high = value

    @property
    def low(self):
        return self._low

    @low.setter
    def low(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('expected a number')
        if value < 0:
            raise ValueError('must be positive')
        self._low = value
        
    # using the @property allows us to not have to use a method call
    # like p.mid() to call the function.
    # Instead, we can just call p.mid  property and it shows the value
    # But we've lost the ability to set this attribute in interactive prompt
    # We would have to build a setter to set the value
    @property
    def mid(self):
        return(self.high + self.low) / 2

    # Since mid is a calculated value, to set it to something else
    # we must change the values of p.high and p.low
    # to recalculate it in the setter . . . cannot change directly
    @mid.setter
    def mid(self, value):
        '''
        recenter around new mid
        keeping constant distance between high and low
        Doc-strings of setters are hard to find
        '''
        distance = (self.high - self.low) / 2
        self.low = value - distance
        self.high = value + distance

    #here's an alternative way to set using a regular method
    # instead of a setter
    def recenter_around_mid(self, value):
        distance = (self.high - self.low) / 2
        self.low = value - distance
        self.high = value + distance        

    def __repr__(self):
        return '{}({},{})'.format(self.__class__.__name__, self.low, self.high)

if __name__ == '__main__':
    p = PriceRange(5, 10)
    print p
