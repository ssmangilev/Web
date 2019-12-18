from urllib.parse import urlparse

def application(environ, start_response):
    if environ['REQUEST_METHOD']=='GET':
        body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    status = '200 OK'
    headers = [
            ('Content-type','text/plain')
            ]
    start_response(status,headers)
    return body
