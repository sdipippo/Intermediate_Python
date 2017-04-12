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

I should look at SQLAlchemy. Does it automate some of the SQL writing?
'''

from collections import MutableMapping
import sqlite3, json

class SqlDict(MutableMapping):
    'dict-like class backed by a sqlite database'
    
    def __init__(self, dbname, *args, **kwargs):
        self.dbname = dbname
        self.connection = sqlite3.connect(dbname)
        c = self.connection.cursor()
        try:
            c.execute('CREATE TABLE Dict (key text, value text)')
            c.execute('CREATE UNIQUE INDEX KeyIndex ON Dict (key)')
        except sqlite3.OperationalError:
            pass # ignore, table already exists
        self.update(*args, **kwargs)

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, etype, e, tb):
        self.close()

    def __repr__(self):
        return '%s(%r, %r)' % (type(self).__name__,
                               self.dbname, self.items())

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
        #import pdb; pdb.set_trace() #quit pdb with 'q'
        c = self.connection.cursor()
        # Note the syntax at the end of the next line. It's for security
        # The execute function itself sanitizes the input when you do this, keeping it secure
        # Execute expects a tuple in this case, (query, input)
        # The "input" is also a tuple (key,), but a single one here
        c.execute('SELECT value FROM Dict WHERE key=?', (key,))
        row = c.fetchone()
        if row is None:
            raise KeyError(key)
        return json.loads(row[0])

    def __delitem__(self, key):
        if key not in self:
            raise KeyError(key)
        c = self.connection.cursor()
        c.execute('DELETE FROM Dict WHERE key=?', (key,))
        self.connection.commit() #if you make a change, you must commit it
        
    def __setitem__(self, key, value):
        if key in self:     # May create race condition, fix with better SQL
                del self[key]
        value = json.dumps(value) # converts ('Rey', 'Finn') to json since tuple is unsupported type
        c = self.connection.cursor()
        c.execute('INSERT INTO Dict VALUES (?, ?)', (key, value))
        self.connection.commit() #if you make a change, you must commit it

if __name__ == '__main__':
    with SqlDict('starwars.db') as d: #starwars is the DB name
        # We are able to use "with" on this class because it has
        # an __enter__ and __exit__ function
        d['hero'] = 'Luke'
        d['villain'] = 'Darth Vader'
        print d
        del d['villain']
        d['hero'] = ('Rey', 'Finn')
        print d
