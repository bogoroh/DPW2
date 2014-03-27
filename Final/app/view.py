class Page(object):
	def __init__(self):
			self.title = "Mike Taatgen - final"
			self.css = '<link rel="stylesheet" href="css/main.css" type="text/css" />'
			self.__header ='''<!DOCTYPE>
<html>
	<head>
        <title>{self.title}</title>
        {self.css}
	</head>
	<body>
		<div id="content">
		<header>
		<h1> Game of Throne Songs </h1>
		
'''   
			self.__closer = '''
		</div>
	</body>
</html>'''
	
	@property
	def header(self):
		return self.__header
	
	@property	
	def close(self):
		return self.__closer

	def update(self):
		self._header = self._header.format(**locals())