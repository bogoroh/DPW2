class ApiView(object):
	def __init__(self,flist):
		self.__content = '''
			<ul>'''
		for l in flist.stations:	
			self.__content += '''
				<li>'''
			self.__content += 'Trainnumber: ' + l["tn"]
			self.__content += l['time']
			self.__content += 'Final Destination: ' + l['fdest']
			self.__content += 'Traintype: ' + l['ttype']
			try:
				self.__content += 'Departure Railway: '  + l['drailway']
			except:
				self.__content += "(railway not available)"

			#content += vhour
			self.__content += '</li>' 
		self.__content += '''
			</ul>'''

	@property
	def content(self):
		return self.__content


class Page(object):
	def __init__(self):
			self.title = "NS - Traininfo"
			self.css = '<link rel="stylesheet" href="css/main.css" type="text/css" />'
			self._header ='''<!DOCTYPE>
<html>
	<head>
        <title>{self.title}</title>
        {self.css}
        <link href='http://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Lustria' rel='stylesheet' type='text/css'>
	</head>
	<body>
		<h1> NS - Traininfo </h1>
		<div id="content">
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

	def update(self):
		self._header = self._header.format(**locals())

class Form(Page):
	# name #Type #labels
	#{"name":"zip","type":"text","label":"Enter your zipcode"}
	def __init__(self,obj):
		super(Form,self).__init__()
		self.method = "GET"
		self.action = ""
		self.__formOpen = '''			<form action="{self.action}" method="{self.method}">'''

		self.__inputs = ''
		for el in obj:
			#print el['name']
			if el['type'] == "text":
				self.__inputs += '''
				<input type="''' + el['type']  + '''" placeholder="''' + el['label'] +'''" name="''' + el['name'] + '''" required="required">'''
			else:
				self.__inputs += '''
				<input type="''' + el['type']  + '''" value="''' + el['label']  +'''" name="''' + el['name'] + '">'''	
		self.__formClose = '''
			</form>'''

	@property
	def getForm(self):
	    return self.__formOpen + self.__inputs + self.__formClose
	
	def update(self):
		self._header = self._header.format(**locals())
		self.__formOpen = self.__formOpen.format(**locals())