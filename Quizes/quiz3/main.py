# Mike Taatgen
# 03 - 20 - 14
# DPW 2 
# Quiz 3

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class Application(object):
	def __init__(self):


class VersionControl(Application):
	def __init__(self):
		super(VersionControl,self).__init__()


class InstantMsg(Application):
	def __init__(self):
		super(InstantMsg,self).__init__()
		
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
