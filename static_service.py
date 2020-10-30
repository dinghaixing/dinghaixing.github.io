import os
import cherrypy

class Imbrium(object):
	def __init__(self):
		pass

	@cherrypy.expose
	def index(self):
		return open("index.html")

if __name__ == '__main__':

	path = os.path.abspath( os.getcwd() )
	
	cherrypy.config.update({
		'server.socket_host': '0.0.0.0',
		'server.socket_port': 801,
		'log.screen': False
	})

	config = { 
		"/": { 
			"tools.sessions.on": True,
			"tools.staticdir.root": path
		},
		'/web': {
			'tools.staticdir.on': True,
			'tools.staticdir.dir': './web',
		},
		'/favicon.ico': {
			'tools.staticfile.on': True,
			'tools.staticfile.filename': path + '/web/img/favicon.ico'
		}
	}

	cherrypy.tree.mount( Imbrium() , '/', config )
	cherrypy.engine.start()
	cherrypy.engine.block()









