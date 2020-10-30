import os
import cherrypy


class Imbrium(object):
	def __init__(self):
		pass

	@cherrypy.expose
	def index(self):
		# return ''' <head><meta http-equiv="refresh" content="0;url=https://dinghaixing.github.io"></head>'''
		return '''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8"/>
  <title>MRC</title>
<style type="text/css">
  body {
    margin: 0;
  }
  iframe {
    display: block; 
    background: #000;
    border: none; 
    height: 100vh; 
    width: 100vw;
  }
</style>
</head>
<body>
<iframe src="https://dinghaixing.github.io/"></iframe>
</body>
</html>
'''
if __name__ == '__main__':
	
	cherrypy.config.update({
		'server.socket_host': '0.0.0.0',
		'server.socket_port': 80,
		'log.screen': False
	})

	config = { 
		"/": { 
			"tools.sessions.on": True,
			"tools.staticdir.root": os.path.abspath( os.getcwd() ) 
		}
		# '/web': {
		# 	'tools.staticdir.on': True,
		# 	'tools.staticdir.dir': './web',
		# },
		# '/favicon.ico': {
		# 	'tools.staticfile.on': True,
		# 	'tools.staticfile.filename': os.path.abspath( os.getcwd() )  + '/web/img/favicon.ico'
		# }
	}

	cherrypy.tree.mount( Imbrium() , '/', config )
	cherrypy.engine.start()
	cherrypy.engine.block()









