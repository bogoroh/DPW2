# Mike Taatgen
# DPW
# Quiz 2

class videos(object):
	actor1 = "Ashton Kutcher"
	actor2 = "Jessica Biel"
	def information():
		_time = "86"
		_rated = "R"
		rating = "4.5"
		return "This movie is " + _time + " minutes long, is rated " + _rated + ", and has a rating of " + rating
	def main_actor(a,b):
		return "The main actors for this movie are " + a + " and " + b

	#Print out the first method
	info = 	information()
	print info

	# Run the second method and print out the second method
	char = main_actor(actor1,actor2)
	print char

	@property
	def time(self):
	    return self._time
	

class soccer(object):
	def information():
		_players = "10"
		_country = "the Netherlands"
		_team = "AFC Ajax"
		return "This team of " + _team + " Consists of " + _players + "Players and this team is from " + _country 

	def current_goalkeeper():
		_goalkeeper = ""
		return "The current Goalkeeper for AFC Ajax is: " + _goalkeeper

	#Print out the first method
	info = 	information()
	print info

	#print out the second methods
	goallie = current_goalkeeper()
	print goallie

	# Setter for goalkeeper
	@goalkeeper.setter
	def goalkeeper(self, value):
	    self._goalkeeper = value
	
