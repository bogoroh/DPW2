# Mike Taatgen
# 03-14-14
# DPW 2
# What does the fox say

import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
