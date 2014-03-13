# Mike Taatgen
# 03-11-14
# DPW2
# Lab 3

import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
