'''
Create something like dictionary, but customized

You can inherit from Collections > MutableMapping to create
a dict-like object backed by the filesystem
- persistent
- concurrent
- introspection
- shareable with other languages
'''

from collections import MutableMapping
import os, pickle

class FileDict(MutableMapping):
    'dict-like, backed by file-system'
    #keys are filenames, values are file data

    def __init__(self, folder, *args, **kwargs):
        try:
            os.mkdir(folder)
        except OSError:
            pass # don't make a folder, it already exists            
        self.folder = folder
        self.update(*args, **kwargs)

    def __repr__(self):
        return '%s(%r, %r)' % (type(self).__name__,
                                   self.folder, self.items())

    def __len__(self):
        len(os.listdir(self.folder))

    def __setitem__(self, key, value):
        #Writes a file (key) and puts data in it (value)
        filepath = os.path.join(self.folder, key)
        with open(filepath, 'w') as f:
            #f.write(repr(value)) #repr represents the tuple as a string
            pickle.dump(value, f)
            
    def __getitem__(self, key):
        filepath = os.path.join(self.folder, key)
        with open(filepath) as f:
            return pickle.load(f)
            #return eval(f.read())

    def __delitem__(self, key):
        filepath = os.path.join(self.folder, key)
        os.remove(filepath)

    def __iter__(self):
        #Iterate through the keys
        return iter(os.listdir(self.folder))
        #optional way to do it
        #for filename in os.listdir(self.folder):
            #yield filename


if __name__ == '__main__':
    d = FileDict('starwars')
    d['hero'] = 'Luke'
    d['villain'] = 'Darth Vader'
    print d

    del d['villain']
    d['hero'] = ('Rey', 'Finn')
    print d
