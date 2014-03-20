class Page(object):
	def __init__(self):
		#Attributes
		self.__id = 1233125 #Private
		self._author = "Mike" #Protected Author
		self.title = "Welcome to the page" # Public acces
		self.head = '''<!DOCTYPE HTML>
<html>
	<head>
		<title></title>
		<link rel="stylesheet" type="text/css" href="css/main.css">
	</head>
    <body>
        '''
		self.body = "Hello World"
		self.form = '''<form method="GET">
        	<input type="text" name="first_name" />
        	<input type="text" name="last_name" />
        	<input type="submit" value="Enter" />
        </form>'''
		self.footer = '''
    </body>
</html> '''
	def print_content():
		print str(self.__id + self._author + self.title)

class Button():
	def __init__(self):
		pass

		