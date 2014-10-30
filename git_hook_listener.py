#!/usr/bin/python
import os
import json
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8000

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_POST(self):
		self.send_response(200)
		self.end_headers()
		# Send the html message
		if self.path == '/stage':
			data_string = self.rfile.read(int(self.headers['Content-Length']))
			data = json.loads(data_string)
			if data['ref'] == "refs/heads/split_alex_requirements":
				os.system('./prepare_ptics')
		return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
