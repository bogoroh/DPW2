# Mike Taatgen
# DPW 2 
# What does the fox say?
# 03 - 18 - 14

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
