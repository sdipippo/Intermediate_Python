'''
a little REST API web server

Our data from our database will now be accessible to
anyone using any language over HTTP because of this rest API
Anyone can call the proper URL to get certain data
'''

from libs import bottle
import docfinder, json

@bottle.route('/')
def welcome():
    return 'Hello, World!'

@bottle.route('/upper/<phrase>')
def to_upper(phrase):
    return phrase.upper()

@bottle.post('/docfinder/v1/document/<uri>')
# We use POST and GET in this and the next method
# instead of 'route' since 'route' doesn't let us distinguish
# between posting and getting
def insert(uri):
    text = bottle.request.POST.get('text', '')
    docfinder.add_document(uri, text)
    data = {'uri': uri, 'text': text}
    bottle.response.content_type = 'application/json'
    return json.dumps(data, indent=2)

@bottle.get('/docfinder/v1/document/<uri>')
def select(uri):
    #See posting to API text file for an example post
    data = {'uri': uri}
    try:
        content = docfinder.get_document(uri)
    except docfinder.UnknownURI as e:
        data['status'] = 'error'
        data['error'] = repr(e)
    else:
        data['status'] = 'OK'
        data['content'] = content
    # below tries to automatically download the text without displaying
    # bottle.response.content_type = 'application/text'
    bottle.response.content_type = 'application/json'
    return json.dumps(data, indent=2)

# host.com/resource?querygoeshere
# localhost:9000/docfinder/v1/document?q=barry,zip
@bottle.route('/docfinder/v1/document')
def search():
    keywords = bottle.request.query.get('q', '').split(',')
    results = docfinder.search(*keywords)
    data = {'status': 'OK',
            'documents': results}
    bottle.response.content_type = 'application/json'
    return json.dumps(data, indent=2)
    

if __name__ == '__main__':
    bottle.run(host='localhost', port=9000)
