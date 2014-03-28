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
			t = i['name']
			self.__nav += '<a href="/?house='+t+'">'+t+'</a>'

	@property
	def nav(self):
	    return self.__nav

class Info(object):
	#pass in the array and the house that was submitted to make content equal to that one
	def __init__(self,house,li):
		for i in li:
			if house == i['name']:
				n = i['name']
				s = i['sigil']
				m = i['motto']
				c1 = i['color1']
				c2 = i['color2']
				h = i['head']
				im = i['image']

				self.__content = ''' 
				<h2> Name: </h2>
				<p>''' + n + ''' </p>
				<h2> Sigil: </h2>
				<p>''' + s+ ''' </p>
				<h2> Motto: </h2>
				<p>''' + m + ''' </p>
				<h2> Color 1: </h2>
				<p>''' + c1 + ''' </p>
				<h2> Color 2 : </h2>
				<p>''' + c2 + ''' </p>
				<h2> Head : </h2>
				<p>''' + h + ''' </p>
				<h2> Image : </h2>
				<img src="http://rebeccacarroll.com/api/got/images/'''+ im + '''" alt="im">'''
	@property
	def content(self):
	    return self.__content