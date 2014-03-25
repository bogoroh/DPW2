# Mike Taatgen
# DPW 2
# 03 - 25 - 14

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
		page = Page()
		form_settings = [{"name":"station","type":"text","label":"Enter the abrevation of the station "},{"name":"submit","type":"submit","label":"Get departure times"}]
		form = Form(form_settings)
		form.update()
		self.response.write(form.header + form.getForm + form.close)
		if self.request.GET:
			print "I ran"
			self.response.write(self.request.GET['station']) 
			self.__station = self.request.GET['station']
			self.__user = 'mtaatgen@live.com' #Authenticator username
			self.__pass = "dv8kZ24iGNZwFiHdZrClS_vaNCKTz1rY5jO9GckIj-fgVEqcgpcyLA"

			self.__url = "http://webservices.ns.nl/ns-api-avt?station=" #URL from the API
			self.__req = urllib2.Request(self.__url + self.__station)
			
			#Creates authentication helper
			password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
			#Binds username and pass to url
			password_manager.add_password(None,self.__url+self.__station,self.__user,self.__pass)
			#Stores user and pass to library's authentication helper
			auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
