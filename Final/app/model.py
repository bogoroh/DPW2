import urllib2
from xml.dom import minidom

class Model(object):
	def __init__(self):
		# Parse the XML to start working with it
		self.file = open("got.xml", 'r')
		self.xml = minidom.parseString(self.file.read())
		
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