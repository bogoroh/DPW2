# Mike Taatgen
# 03 - 20 - 14
# DPW 2 
# Quiz 3

import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hello world!')

		#test out our superclass
		app = Application()
		print app.stable(app.version)
		print app.compatible("MAC")

		#test out our subclass #1
		sub1 = VersionControl()
		print "This is what VersionControl does:"
		print sub1._do


		#test out our subclass #2
		sub2 = InstantMsg()
		print "This is what the InstantMsg does:"
		print sub2._do

#Superclass
class Application(object):
	def __init__(self):
		self.__name = "Application"
		self._version = 1.235
		self._do = "An application can do everything. Let's try to get more deeper shall we?" #attribute we are going to overwrite

	def stable(self,v):
		if v > 1.0:
			return "True"
		else:
			return "False"

	def compatible(self,m):
		if m == "MAC" or m == "mac":
			return "This application is compatible with your pc (MAC)."
		else:
			return "Sorry, This application is not compatible with MAC. Please come back to check if we have a new version for you?"

	@property
	def name(self):
	    return self.__name

	@property
	def version(self):
	    return self._version

	
#Subclass #1
class VersionControl(Application):
	def __init__(self):
		super(VersionControl,self).__init__()
		self._use = "As a collaboration or solo"
		self._do = "Make commits, collaborate and save your commits. "

	@property
	def use(self):
	    return self._use

#Subclass #2
class InstantMsg(Application):
	def __init__(self):
		super(InstantMsg,self).__init__()
		self._chat  = "By video or by messaging"
		self._screenname = "Jerry"
		self._do = "Send video,chat or emoticons over the net."

	@property
	def chat(self):
	    return self._chat
	
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
