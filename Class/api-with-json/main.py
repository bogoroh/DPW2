# Mike Taatgen
# DPW
# 03/18/2014
# Day 5 - Yahoo Weather API Minidom

import webapp2
import urllib2 # need this for requesting info from API
#import xml.etree.ElementTree as ET # library for working with xml in python
import json

class MainHandler(webapp2.RequestHandler):
	def get(self):
		# if there is info in the URL (the loc code in this case)
		if self.request.GET:
			loc = self.request.GET['loc']
			url = "http://api.openweathermap.org/data/2.5/weather?q="

			request = urllib2.Request(url + loc) # assemble request
			opener = urllib2.build_opener() # use urllib2 to create an object to get the url
			result = opener.open(request) # use url to get a result - request info from api

			# parse the result
			json_doc = json.load(result)
			self.response.write(json_doc) 
			'''
			xmldoc = ET.parse(result)
			root = xmldoc.getroot()
			
			content = "<br />"
			#content += root[0][12][7].attrib['day'].text
			for i in root.iter('{'+namespace+'}:forecast'):
				content += i.attrib['day'] + "----High:" + i.attrib['high']
				content += "<br/>"
			self.response.write(content)'''

		else:
			page = FormPage()
			page.inputs = {"loc":"text", "Submit":"submit"}
			page.create_inputs()

			self.response.write(page.print_out("Enter your City and state:"))

class Page(object):
	def __init__(self):
		self._header = '''<!DOCTYPE html>
		<html lang="en">
			<head>
				<meta charset="utf-8">
				<title>Day 5 | Yahoo Weather API</title>
			</head>
			<body>
				<h1>Day 5</h1>'''

		self._body = ''

		self._footer = '''
		</body>

		<footer>
			<p>Copyright &copy; 2014 <strong>Day 5</strong></p>
		</footer>
	</html>'''

	@property
	def body(self):
		pass

	@body.setter
	def body(self, b):
		self._body = b

	def print_out(self):
		return self._header + self._body + self._footer

class FormPage(Page):
	def __init__(self):
		#run the instantiating function for the Super Class
		super(FormPage, self).__init__()
		self.__form_open = "<form method='GET'>"

		self.__form_close = "</form>"

		self.__inputs = dict()
		self.__input_string = ""

	def create_inputs(self):
		for key, value in self.__inputs.iteritems():
			print key
			self.__input_string += "<input type='" +value+ "' name='"+key+"' /><br />"

	def print_out(self, msg):
		return self._header + msg + self.__form_open + self.__input_string + self.__form_close + self._footer

	@property
	def inputs(self):
		pass

	@inputs.setter
	def inputs(self, dict):
		self.__inputs = dict

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)