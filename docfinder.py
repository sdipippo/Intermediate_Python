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
    text        text

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
    return [(term, count / total) for term, count in counts]
    
def add_document(uri, text):
    '''
    Insert a new document into the database with the given URI
    '''
    
def get_document(uri):
    '''
    Retrieve the content of a document specified by URI
    '''
    
def search(*keywords):
    '''
    List URIs of relevant documents
    '''
