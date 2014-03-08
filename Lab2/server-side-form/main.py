# Mike Taatgen
# DPW
# Server Side Form
# 03/08/14

import webapp2
from page import *

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
