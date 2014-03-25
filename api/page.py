class Page(object):
	def __init__(self):
			self.title = "NS - Traininfo"
			self.css = '<link rel="stylesheet" href="css/main.css" type="text/css" />'
			self._header ='''<!DOCTYPE>
<html>
    <head>
        <title>{self.title}</title>
        {self.css}
    </head>
<body>
       '''   
			self.__closer = '''
</body>
</html>'''
	
	@property
	def header(self):
		return self._header
	
	@property	
	def close(self):
		return self.__closer

	def update(self):
		self._header = self._header.format(**locals())		