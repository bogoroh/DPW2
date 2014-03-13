class Page():
	def __init__(self):
		self.__header = '''
<!DOCTYPE>
<html>
<head>
<title>Phone Calculator</title>
<link rel="stylesheet" href="css/main.css">
</head>
<body>
'''
        
		self.__form = '''

'''
        
		self.__footer = '''

'''
	@property
    def header(self):
        return self.__header

    @property
    def form(self):
        return self.__form

    @property
    def footer(self):
        return self.__footer