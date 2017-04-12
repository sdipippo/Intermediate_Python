'''
abstract.py
Playing with magics to skip every other element

Mixin - small classes that are meant to be inherited but
not meant to do anything by itself
Programming is as easy as writing a list of capabilities
    It is too easy to accidentally instantiate a Mixin
    And it's too easy to forget to implement the required methods
Solution: ABCs (Abstract Base Class)
    Enforces / solves the problem of Mixins
    Cannot be instantiated.
    None of an ABCs children can be instantiated unless they
     implement the required methods

'''
from abc import ABCMeta, abstractmethod
from collections import Sequence

class Capper:
    'inherit to gain uppercasing capability'
    ' Here we create an ABC that requires two abstract methods'
    ' that must be created to use this class'
    __metaclass__ = ABCMeta
    
    def capitalize(self):
        return ''.join([c.upper() for c in self])

    @abstractmethod
    def __getitem__(self, index):
        return None

    @abstractmethod
    def __len__(self):
        return 0

class Uncapper(Sequence):
    'inherit to gain lowercasing capability'
    ' Sequence is an ABC already, so this class inherits'
    ' The Parent ABC requirements to work (__getitem__ and __len__)'
    ' Must be defined before it will work '
    def uncapitalize(self):
        return ''.join([c.lower() for c in self])

class SkipSeq(Capper, Uncapper):
    '''
    Sequence that skips every other element.

        >>> skip = SkipSeq('abcdefg')
        >>> skip[0]
        'a'
        >>> skip[1]
        'c'
        >>> len(skip)
        4
    '''

    def __init__(self, sequence):
        self.seq = sequence

    def __getitem__(self, index):
        return self.seq[index * 2]

    def __len__(self):
        return (len(self.seq) + 1) // 2

class SkipTwoSeq(Capper, Uncapper):
    '''
    Sequence that keeps every third element

        >>> skip = SkipTwoSeq('abcdefg')
        >>> skip[0]
        'a'
        >>> skip[1]
        'd'
        >>> len(skip)
        3
    '''
    def __init__(self, sequence):
        self.seq = sequence

    def __getitem__(self, index):
        return self.seq[index * 3]
    
    def __len__(self):
        return (len(self.seq) + 2) // 3

if __name__ == '__main__':
    #doctest tests docstrings only against the code
    import doctest
    doctest.testmod()
