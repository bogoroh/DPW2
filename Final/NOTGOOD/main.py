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
        self.response.write('Hello world!')


        # Let's create an instance of Models
        model = Model()


        # Let's create the page
        page = Page ()
        self.response.write(page.header)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
