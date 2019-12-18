from urllib.parse import urlparse

def wsgi_app(environ, start_response):
    if environ['REQUEST_METHOD']=='GET':
        body = environ['QUERY_STRING'].replace('&','\n')
    status = '200 OK'
    headers = [
            ('Content-type','text/plain')
            ]
    start_response(status,headers)
    return [body]
