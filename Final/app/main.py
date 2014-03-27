# Mike Taatgen
# DPW 2
# 03 - 27 - 14

import webapp2
import urllib2
from xml.dom import minidom
from model import *
from view import *

class MainHandler(webapp2.RequestHandler):
    def get(self):
		# Let's create an instance of Models
		model = Model()
		self.response.write(model.houseArr)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
