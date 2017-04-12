'''
abstract.py
Playing with magics to skip every other element
'''

class Capper:
    'inherit to gain uppercasing capability'
    def capitalize(self):
        return ''.join([c.upper() for c in self])

class Uncapper:
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
