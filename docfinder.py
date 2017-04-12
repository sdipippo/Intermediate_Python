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

class UnknownURI(Exception):
    'uri not found'

class DuplicateURI(Exception):
    'uri already exists'

stopwords = {'the', 'and', 'of', 'is'}

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

def score_document(text, n=200, pattern=r'[a-z]+'):
    '''
    Calculate relevance scores for the 'n'
    most frequent terms in a text
    '''
    
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
