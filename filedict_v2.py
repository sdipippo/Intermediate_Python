''' filedict.py

dict-like, backed by the filesystem
- persistent
- concurrent
- introspectable
- shareable with other languages
'''

from collections import MutableMapping
import os, pickle

class FileDict(MutableMapping):
    'dict-like, backed by the filesystem'
    # keys are file names
    # values are file data

    def __init__(self, folder, *args, **kwargs):
        try:
            os.mkdir(folder)
        except OSError:
            pass # ignore, folder exists
        self.folder = folder
        self.update(*args, **kwargs)

    def __repr__(self):
        return '%s(%r, %r)' % (type(self).__name__,
                               self.folder, self.items())

    def __getitem__(self, key):
        filepath = os.path.join(self.folder, key)
        try:
            with open(filepath) as f:
                return pickle.load(f)
        except IOError:
            raise KeyError(key)

    def __setitem__(self, key, value):
        filepath = os.path.join(self.folder, key)
        with open(filepath, 'w') as f:
            pickle.dump(value, f)

    def __delitem__(self, key):
        filepath = os.path.join(self.folder, key)
        try:
            os.remove(filepath)
        except OSError:
            raise KeyError(key)

    def __iter__(self):
        return iter(os.listdir(self.folder))

    def __len__(self):
        return len(os.listdir(self.folder))

if __name__ == '__main__':
    d = FileDict('starwars')
    d['hero'] = 'Luke'
    d['villain'] = 'Darth Vader'
    print d

    del d['villain']
    d['hero'] = ('Rey', 'Finn')
    print d
