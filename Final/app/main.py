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

		# Let's create the page
		page = Page()
		link = Links(model.houseArr)
		self.response.write(page.header + link.nav + page.close)


		if self.request.GET:
			house = self.request.get('house')

			info = Info(house,model.houseArr)
			self.response.write(info.content)
		# Display nothing but the links

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
