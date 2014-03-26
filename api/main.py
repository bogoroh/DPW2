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
		form_settings = [{"name":"station","type":"text","label":"Enter your station names "},{"name":"submit","type":"submit","label":"Get departure times"}]
		form = Form(form_settings)
		form.update()

		if self.request.GET:
			#self.response.write(self.request.GET['station']) 
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
			self.__station = self.__sresponse
			aModel = ApiModel(self.__station)
			aView = ApiView(aModel.do())
			self.response.write(aView.content)
			
class ApiModel(object):
	'''This class handles fetching,parsing and sorting data from the weather api'''
	def __init__(self,self.__station):
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

		#creates "openeer object for fetching page info"
		self.__opener = urllib2.build_opener(auth_manager)
		self.send()

	def send(self):		
		urllib2.install_opener(self.__opener)
		handler = urllib2.urlopen(self.__req)
		openerURL = urllib2.build_opener() #magic to load request - creates framework to get url
		result = openerURL.open(self.__req) # gets url and puts result in "result"
		self.sort()

	def sort(self):
		xmldoc = minidom.parse(result) #parse through string to get XML object
		self.__do = ApiData()
		ARit = xmldoc.getElementsByTagName('RitNummer')
		AVertrekTijd = xmldoc.getElementsByTagName('VertrekTijd') # Saved the departure time for that station into an array
		AEind = xmldoc.getElementsByTagName('EindBestemming') # Saves all the final destination into an array  for that station
		ATrein = xmldoc.getElementsByTagName('TreinSoort') # Saves all the Traintypes in an array for that station
		AVertrek = xmldoc.getElementsByTagName('VertrekSpoor') #Saves all the Departure railways for that station into an array 		

		if ARit:
				for l,m,n,o,p in zip(ARit, AVertrekTijd,AEind,ATrein,AVertrek): # Makes it possible to loop throught multiple arrays
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
					else:
						prefix = "am"

					
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
					tempDict['time'] = 'Departure Time: ' + d + " " + vmonth  + " " + y + " at " + str(hourv) + ":" + m +prefix
					tempDict['fdest'] = fd
					tempDict['ttype'] = tt
					tempDict['drailway'] = dr
					self.__do.stations.append(tempDict)

	def do(self):
		return self__do

class ApiData(object):
	''' This class holds the data taken from the api'''
	def __init__(self):
		self.stations = [] #Array that will hold all the info

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
