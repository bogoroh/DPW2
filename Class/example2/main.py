
import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
        self.page = Page()
        self.response.write(self.page.all)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
