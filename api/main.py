# Mike Taatgen
# DPW 2
# 03 - 25 - 14

import webapp2
from page import *
import urllib2 #Needed for importing from URL's
from xml.dom import minidom #convert XML into an object

class MainHandler(webapp2.RequestHandler):
    def get(self):
		page = Page()
		form_settings = [{"name":"station","type":"text","label":"Enter your station name "},{"name":"submit","type":"submit","label":"Get departure times"}]
		form = Form(form_settings)
		form.update()
		
		if self.request.GET:
			self.rstation = self.request.GET['station'].lower()
			if self.rstation == "alkmaar":
				self.__sresponse = "amr"
			elif self.rstation == "apeldoorn":
				self.__sresponse = "apd"
			elif self.rstation == "breda":
				self.__sresponse = "bd"
			elif self.rstation == "delft": 
				self.__sresponse = "dt"
			elif self.rstation == "emmen": 
				self.__sresponse = "emn"
			elif self.rstation == "gouda": 
				self.__sresponse = "gd"
			elif self.rstation == "haarlem": 
				self.__sresponse = "hlm"
			else:
				self.__sresponse =  self.request.GET['station']
			aModel = ApiModel(self.__sresponse)
			aView = ApiView(aModel.do)

			if aModel.ARit:
				self.response.write(form.header + form.getForm + aView.content + form.close)
			else:
				invalid = '''
			<h2>Please input a valid station</h2>'''
	  			self.response.write(form.header + form.getForm + invalid + form.close)
	  	else:
	  		self.response.write(form.header + form.getForm + form.close)

class ApiModel(object):
	'''This class handles fetching,parsing and sorting data from the weather api'''
	def __init__(self,station):
		self.__user = 'mtaatgen@live.com' #Authenticator username
		self.__pass = "dv8kZ24iGNZwFiHdZrClS_vaNCKTz1rY5jO9GckIj-fgVEqcgpcyLA"
		self.__url = "http://webservices.ns.nl/ns-api-avt?station=" #URL from the API
		self.__req = urllib2.Request(self.__url + station)
		#Creates authentication helper
		password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
		#Binds username and pass to url
		password_manager.add_password(None,self.__url+ station,self.__user,self.__pass)
		#Stores user and pass to library's authentication helper
		auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)

		#creates "openeer object for fetching page info"
		self.__opener = urllib2.build_opener(auth_manager)
		self.send()

	def send(self):		
		urllib2.install_opener(self.__opener)
		handler = urllib2.urlopen(self.__req)
		openerURL = urllib2.build_opener() #magic to load request - creates framework to get url
		self.__result = openerURL.open(self.__req) # gets url and puts result in "result"
		self.sort()

	def sort(self):
		self.__xmldoc = minidom.parse(self.__result) #parse through string to get XML object
		self.__do = ApiData()
		self.__ARit = self.__xmldoc.getElementsByTagName('RitNummer')
		AVertrekTijd = self.__xmldoc.getElementsByTagName('VertrekTijd') # Saved the departure time for that station into an array
		AEind = self.__xmldoc.getElementsByTagName('EindBestemming') # Saves all the final destination into an array  for that station
		ATrein = self.__xmldoc.getElementsByTagName('TreinSoort') # Saves all the Traintypes in an array for that station
		AVertrek = self.__xmldoc.getElementsByTagName('VertrekSpoor') #Saves all the Departure railways for that station into an array 		

		if self.__ARit:
			for l,m,n,o,p in zip(self.__ARit, AVertrekTijd,AEind,ATrein,AVertrek): # Makes it possible to loop throught multiple arrays
				tnv = l.firstChild.nodeValue
				y = m.firstChild.nodeValue[:4]
				amonth = m.firstChild.nodeValue[5:7]
				d = m.firstChild.nodeValue[8:10]
				vhour = m.firstChild.nodeValue[11:13]
				m = m.firstChild.nodeValue[14:16]
				fd = n.firstChild.nodeValue
				tt = o.firstChild.nodeValue
				dr = p.firstChild.nodeValue
				if int(vhour) > 12:
					prefix = "pm"
					hourv = int(vhour) - 12
				elif int(vhour) == 12:
					prefix = "pm"
					hourv = int(vhour)
				else:
					prefix = "am"
					hourv = int(vhour)
			
				if amonth == "01":
					vmonth = "January"
				elif amonth == "02":
					vmonth = "February"
				elif amonth == "03":
					vmonth = "March"
				elif amonth == "04":
					vmonth = "April"
				elif amonth == "05":
					vmonth = "May"
				elif amonth == "06":
					vmonth = "June"
				elif amonth == "07":
					vmonth = "July"
				elif amonth == "08":
					vmonth = "August"
				elif amonth == "09":
					vmonth = "September"
				elif amonth == "10":
					vmonth = "October"
				elif amonth == "11":
					vmonth = "November"
				else:
					vmonth = "December"

				tempDict = dict() # Creates the set of info
				tempDict['tn'] = tnv
				tempDict['time'] = 'Departure Time: ' + "<span class='timebox'>" +  d + "</span>" + " " + vmonth  + " " + y + " at " + "<span class='timebox'>" +str(hourv) + "</span>"+ ":" + "<span class='timebox'>" + m + "</span>" + "<span class='timebox'>" + prefix + "</span>"
				tempDict['fdest'] = fd
				tempDict['ttype'] = tt
				tempDict['drailway'] = dr
				self.__do.stations.append(tempDict)

	@property
	def do(self):
		return self.__do

	@property
	def ARit(self):
		return self.__ARit

class ApiData(object):
	''' This class holds the data taken from the api'''
	def __init__(self):
		self.stations = [] #Array that will hold all the info

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
