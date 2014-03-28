import urllib2
from xml.dom import minidom

class Model(object):
	"""docstring for Model where we will be getting all the XML data for the assignement"""
	def __init__(self):
		self.__xmldoc = minidom.parse(open('http://rebeccacarroll.com/api/got/got.xml',"r"))
		self.__house = self.__xmldoc.getElementsByTagName("house")