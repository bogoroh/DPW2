# Mike Taatgen
# 03-11-14
# DPW2
# Lab 3

import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
	def get(self):
		page = Page() # creates an instance of the Page function which is defined at library.py

		mike = Person(5555) # Password for his/her voicemail
		mike.name = "Mike Taatgen" # Name of the user
		mike.text = 45 #Amount of text send
		mike.minutes = 300 # Amount of minutes talked on the phone
		mike.internet =  2 # Amount of GB used for data

		anthony = Person(5235) # Password for his/her voicemail
		anthony.name = "Anthony Kluba" # Name of the user
		anthony.text = 25 #Amount of text send
		anthony.minutes = 325 # Amount of minutes talked on the phone
		anthony.internet = 7.2 # Amount of GB used for data

		nate = Person(1821) # Password for his/her voicemail
		nate.name = "Nathan Dickison" # Name of the user
		nate.text = 75 #Amount of text send
		nate.minutes = 290 # Amount of minutes talked on the phone
		nate.internet = 3.2 # Amount of GB used for data

		jairo = Person(8371) # Password for his/her voicemail
		jairo.name = "Jairo Jurado" # Name of the user
		jairo.text = 25 #Amount of text send
		jairo.minutes = 400 # Amount of minutes talked on the phone
		jairo.internet =  6 # Amount of GB used for data

		rebecca = Person(9213) # Password for his/her voicemail
		rebecca.name = "Rebecca Carroll" # Name of the user
		rebecca.text = 49 #Amount of text send
		rebecca.minutes = 280 # Amount of minutes talked on the phone
		rebecca.internet = 4 # Amount of GB used for data

		players = [mike,anthony,nate,jairo,rebecca]	#array with all the players

		self.response.write(page.header()) # Creates the HTML attributes
		self.response.write(page.form())
		if self.request.GET:
			player = int(self.request.GET['person'])-1 #because index start at 0 
			self.response.write(self.html(players[player]))
		self.response.write(page.footer())

	def html(self,player):
		total = (player.text * .25) + (player.minutes * 0.04) + (player.internet * 8.5)
		code = '''
		<h1>{player.name}</h1>
		<div>
			<div>
				<h2>Amount of texts</h2>
				<span>{player.text} Texts</span>
			</div>
			<div>
				<h2>Amount of minutes talked</h2>
				<span>{player.minutes} Minutes</span>
			</div>
			<div>
				<h2>Amount of GB used for data</h2>
				<span>{player.internet} GB</span>
				<span> <progress value="{player.internet}" max="10"></progress> </span>
			</div>
			<div>
				<h2>Monthly fee</h2>
				<span>{total}$</span>
			</div>
		</div>'''	
		code = code.format(**locals())
		return code		
class Person(object):
	def __init__(self,pin):
		self.name = ""
		self.text = 0
		self.minutes = 0
		self.__internet = 0
		self.__password = pin
		
	#GETTER FUNCTION	
	@property 
	def password(self):
		return self.__password	
		
	# SETTER FUNCTION	
	#setters can do more
	@password.setter
	def internet(self,value):
		self.__password = value

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
