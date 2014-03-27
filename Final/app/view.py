class Page(object):
	def __init__(self):
		self._header ='''<!DOCTYPE>
<html>
	<head>
        <title>Mike Taatgen - final</title>
        <link rel="stylesheet" href="css/main.css" type="text/css" />
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
		return self._header
	
	@property	
	def close(self):
		return self.__closer

class Links(object):
	def __init__(self,li):
		self.__nav = ''
		for i in li:
			self.__nav += '<a href="/?house='+i+'">'+i+'</a>'	