#
import webapp2
from page import *

#Beginning of the code
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hello Mike!')
        print "Hi"
        page = Page()
        
       	#self.response.write(head + body + form +  footer)
        if self.request.GET:
        	info = self.request.GET["first_name"] + " " + self.request.GET["last_name"] 
        	self.response.write(page.head+ info +page.footer)
        else:
        	self.response.write(page.head+page.body+page.form+page.footer)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
