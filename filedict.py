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
import os

class FileDict(MutableMapping):
    'dict-like, backed by file-system'
    #keys are filenames, values are file data

    def __init__(self, folder):
        self.folder = folder

    def __len__(self):
        len(os.listdir(self.folder))

    def __setitem__(self, key, value):
        #Writes a file (key) and puts data in it (value)
        filepath = os.path.join(self.folder, key)
        with open(filepath, 'w') as f:
            f.write(value)

    def __getitem__(self, key):
        filepath = os.path.join(self.folder, key)
        with open(filepath) as f:
            return f.read()

    
    

if __name__ == '__main__':
    d = FileDict('starwars')
    d['hero'] = 'Luke'
    d['villain'] = 'Darth Vader'
    print d

    del d['villain']
    d['hero'] = ('Rey', 'Finn')
    print d
