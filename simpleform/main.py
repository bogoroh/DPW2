#
import webapp2


#Beginning of the code
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello Mike!')
        print "Hi"

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
