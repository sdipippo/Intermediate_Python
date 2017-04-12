'''
dict-like, backed by a sqlite database.
- persistence
- concurrent
- shareable with other languages
- introspectable

    Dict    data type
    ===================
    key     text    <-- unique index
    value   text
'''

from collections import MutableMapping
import sqlite3, json

class SqlDict(MutableMapping):
    'dict-like class backed by a sqlite database'
    
    def __init__(self, dbname):
        self.dbname = dbname
        self.connection = sqlite3.connect(dbname)

    def __len__(self):
        # similar to file handle, allows us to do things to the DB connection
        c = self.connection.cursor()
        c.execute('SELECT count(key) FROM Dict') #query DB and return cursor
        row = c.fetchone()
        return row[0]

    def __iter__(self):
        c = self.connection.cursor()
        c.execute('SELECT key FROM Dict')
        rows = c.fetchmany()
        return (key for (key,) in rows)

    def __getitem__(self, key):
        c = self.connection.cursor()
        # Note the syntax at the end of the next line. It's for security
        # The execute function itself sanitizes the input when you do this, keeping it secure
        # Execute expects a tuple in this case, (query, input)
        # The "input" is also a tuple (key,), but a single one here
        c.execute('SELECT value FROM Dict WHERE key=?', (key,))
        row = c.fetchone()
        return row[0]

    def __delitem__(self, key):
        c = self.connection.cursor()
        c.execute('DELETE FROM Dict WHERE key=?', (key,))
        self.connection.commit() #if you make a change, you must commit it
        
    def __setitem__(self, key, value):        
        c = self.connection.cursor()
        c.execute('INSERT INTO Dict VALUES (?, ?)', (key, value))
        self.connection.commit() #if you make a change, you must commit it

if __name__ == '__main__':
    d = SqlDict('starwars.db') #starwars is the DB name
    d['hero'] = 'Luke'
    d['villain'] = 'Darth Vader'
    print d
    del d['villain']
    d['hero'] = ('Rey', 'Finn')
    print d
