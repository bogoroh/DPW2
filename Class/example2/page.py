class Page(object):
	def __init__(self):
		self.header ='''<!DOCTYPE>
<html>
    <head>
        <title>{self.__title}</title>
    </head>
    <body>
       '''
		self.body = ""
		self.close = '''
</body>
</html> '''
		self.all = ""
		self.__title = "Welcome"

	def update_page(self):
		self.all = self.header + self.body + self.close

	@property
	def title(self):
	    return self.__title
	@title.setter
	def title(self, value):
	    self.__title = value
	

	  
