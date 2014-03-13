class Page():
	def __init__(self):
		self.__header = '''
<!DOCTYPE>
<html>
<head>
<title>Phone Calculator</title>
<link rel="stylesheet" href="css/main.css">
<script src="js/jquery.js" type="text/javascript"></script>  
<script src="js/main.js" type="text/javascript"></script>  
</head>
<body>
'''
        
		self.__form = '''
	<form method="GET" action="" name="players" id="links">
		<a href="/?person=1" name="person" id="Mike Taatgen">Mike Taatgen</a>
		<a href="/?person=2" name="person" id="Anthony Kluba">Anthony Kluba</a>
		<a href="/?person=3" name="person" id="Nathan Dickison">Nathan Dickison</a>
		<a href="/?person=4" name="person" id="Jairo Jurado">Jairo Jurado</a>
		<a href="/?person=5" name="person" id="Rebecca Carroll">Rebecca Carroll</a>
	</form>
'''
        
		self.__footer = '''
</body>

'''
		
	def header(self):
	    return self.__header

	
	def form(self):
	    return self.__form

	
	def footer(self):
	    return self.__footer