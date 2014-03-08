# Mike Taatgen
# DPW
# Server Side Form
# 03/08/14

import webapp2
from page import *

class MainHandler(webapp2.RequestHandler):
    def get(self):
        title = "Welcome voter!"
        page = Page() # Creates an instance of the imported class page
        self.response.write(page.head(title))
        
        #if there is a URL variable then print this
        if self.request.GET:
	        myList = self.request.get_all("member") #get_all makes them a list 
	        myString = ",".join(myList ) # seperates the list with commas so that you can put it inside the write function function as a string
        	self.response.write("Thank you for your vote" + " " + self.request.GET["fName"] + " " + self.request.GET["lName"] +"(" + self.request.GET["sex"] + ")" + ", Born on " + self.request.GET["bday"] + "th" + " of " + self.request.GET["bmonth"] + " " + self.request.GET["byear"] + ". You have voted for the following members:" +myString )
        
        else:
        	self.response.write(page.registration())
#         self.response.write(form)
        self.response.write(page.close())
        #p = p.format(**locals())
        #self.response.write(p)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
