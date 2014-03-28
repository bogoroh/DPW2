import urllib2
from xml.dom import minidom

class Model(object):
	def __init__(self):
		# Parse the XML to start working with it
		self.url = "http://rebeccacarroll.com/api/got/got.xml"
		self.reg = urllib2.Request(self.url)
		opener = urllib2.build_opener() #magic to load request 
		self.result = opener.open(self.reg) # gets url and puts result in "result"
		self.xml = minidom.parse(self.result)
		
		#Array that holds all the information
		self.houseArr = []

		house = self.xml.getElementsByTagName("house")
		for h in house:
			tempDict = dict()
			tempDict['name'] = h.getElementsByTagName('name')[0].firstChild.nodeValue
			tempDict['sigil'] = h.getElementsByTagName('sigil')[0].firstChild.nodeValue 
			tempDict['motto'] = h.getElementsByTagName('motto')[0].firstChild.nodeValue 
			tempDict['color1'] = h.getElementsByTagName('color1')[0].firstChild.nodeValue 
			tempDict['color2'] = h.getElementsByTagName('color2')[0].firstChild.nodeValue
			tempDict['head'] = h.getElementsByTagName('head')[0].firstChild.nodeValue
			tempDict['image'] = h.getElementsByTagName('image')[0].firstChild.nodeValue
			self.houseArr.append(tempDict)