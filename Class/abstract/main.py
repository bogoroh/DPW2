import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		fp = FormPage()
		fp.inputs = {"first_name": "text", "last_name": "text"}
		fp.create_inputs()
		self.response.write(fp.print_out())

class Page(object):
	def __init__(self):
		self._head = '''<!DOCTYPE HTML>
		<html>
		<head>
		<title>{self.title}</title>
		</head>
		<body>
		'''
		self._body = ''' '''
		self._close = '''
		</body>
		</html>
		'''

class FormPage(Page):
	def __init__(self):
		super(FormPage, self).__init__()
		self.__form_open = '<form method="GET">'
		self.__form_close = '</form>'
		self.__inputs = dict()
		self.__input_string = ''

	def create_inputs(self):
		for i in self.__inputs:
			# i - key
			# self.__inputs[i] - value
			self.__input_string += '<input type="' + self.__inputs[i] + '" name="' + i + '">'

	def print_out(self):
		return self._head + self.__form_open + self.__input_string + self.__form_close + self._close

	@property
	def inputs(self):
		pass
	@inputs.setter
	def inputs(self, dict):
		self.__inputs = dict

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

