'''docfinder
Keyword-searchable document database


API:

    create_db(force=False) # force recreation of database, by default false
    add_document(uri, text) --> None
    search(keyword0, keyword1, etc. . . ) --> list of URIs (Uniform resource identifiers)
    get_document(URI) --> text of the document
    
    Errors: DuplicateURI, UnknownURI


Table:

    Documents
    ==========================
    uri         text    <-- unique index
    text        blob

    Scores
    ==========================
    uri         text
    term        text    <-- index
    score       real

Relevance score = term frequency / total words in document

'''

from __future__ import division
from collections import Counter
from contextlib import closing #helps close connections
import sqlite3, os, re
import bz2 #compresses large information, similar to gzip

# These are the public interface of the module
# If someone imports *, they get the below modules
# It's also a good indication of what functions should be used
# by you if you are a user
__all__ = ['create_db',
           'add_document',
           'get_document',
           'search',
           'UnknownURI',
           'DuplicateURI']

class UnknownURI(Exception):
    'uri not found'

class DuplicateURI(Exception):
    'uri already exists'

stopwords = {'the', 'and', 'of', 'is'}
database = 'pepsearch.db'

def create_db(force=False): # force recreation of database, by default false
    '''
    Create a new document database.
    Delete the old one if "force = True"
    '''
    if force:
        try:
            os.remove(database)
        except OSError:
            pass # ignore, does not exist
    #closing is a module we are using to make this connection "withable"
    with closing(sqlite3.connect(database)) as connection:
        c = connection.cursor()
        c.execute('CREATE TABLE Documents (uri text, text blob)')
        c.execute('CREATE TABLE Scores (uri text, term text, score real)')
        c.execute('CREATE UNIQUE INDEX UriIndex ON Documents(uri)')
        c.execute('CREATE INDEX TermIndex ON Scores(term)')

def normalize(words):
    '''
    Transform words into standardized terms by lowercasing,
    de-pluralizing, and ignoring stopwords
    '''
    normalized_words = []
    for word in words:
        lowercased = word.lower()
        if lowercased not in stopwords:
            singular = lowercased.rstrip('s')
            normalized_words.append(singular)
    return normalized_words

    # lowercased = [word.lower() for word in words]
    # return [word.rstrip('s') for word in lowercased if word not in stopwords]
        

def score_document(text, n=200, pattern=r'[A-Za-z]+'):
    '''
    Calculate relevance scores for the 'n'
    most frequent terms in a text
    '''
    words = re.findall(pattern, text)
    terms = normalize(words)
    counts = Counter(terms).most_common(n)
    # passing something to Counter creates a dictionary of counts
    total = len(terms)
    return ((term, count / total) for term, count in counts)
    
def add_document(uri, text):
    '''
    Insert a new document into the database with the given URI
    '''
    blob = sqlite3.Binary(bz2.compress(text)) # Let sqlite3 know this is binary and not text, and compress it
    with closing(sqlite3.connect(database)) as connection:
        c = connection.cursor()
        try:
            c.execute('INSERT INTO Documents VALUES (?, ?)', (uri, blob))
        except sqlite3.IntegrityError:
            raise DuplicateURI(uri)

        '''
        for term, score in score_document(text):
            c.execute('INSERT INTO Scores VALUES (?, ?, ?)', (uri, term, score))
        '''

        args = ((uri, term, score) for term, score in score_document(text))
        c.executemany('INSERT INTO Scores VALUES (?, ?, ?)', args)
        
        connection.commit()
    
def get_document(uri):
    '''
    Retrieve the content of a document specified by URI
    '''
    with closing(sqlite3.connect(database)) as connection:
        c = connection.cursor()
        c.execute('SELECT text FROM Documents WHERE uri=?', (uri,))
        row = c.fetchone()
        if row is None:
            raise UnknownURI(uri)
        return bz2.decompress(row[0])


    
def search(*keywords):
    '''
    List URIs of relevant documents
    '''
    terms = normalize(keywords)
    query_template = '''
    SELECT uri
    FROM Scores
    WHERE term IN ({})
    GROUP BY uri
    ORDER BY sum(score) DESC
    '''
    marks = '?' * len(terms)
    query = query_template.format(', '.join(marks))
    with closing(sqlite3.connect(database)) as connection:
        c = connection.cursor()
        c.execute(query, terms) 
        rows = c.fetchall()
        return [uri for (uri,) in rows]
