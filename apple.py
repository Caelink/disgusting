#!/usr/bin/python

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
	return Response('Hello %(name)s!' % request.matchdict)

def disgusting(request):
	return Response('Disgusting!')

if __name__ == '__main__':
	config = Configurator()
	config.add_route('hello', '/hello/{name}')
	config.add_view(hello_world, route_name='hello')
	config.add_route('disgusting', '/disgusting')
	config.add_view(disgusting, route_name='disgusting')
	app = config.make_wsgi_app()
	server = make_server('0.0.0.0', 8080, app)
	server.serve_forever()
