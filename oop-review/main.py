
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.luke = Character()
        self.luke.name = "Luke Skywalker"
        self.luke.profession = "Jedi"
        self.luke.age = 19
        self.luke.speak()

        self.leia = Character()
        self.leia.name = "Leia Organa"
        self.leia.profession = "Princess"
        self.leia.age = self.luke.age 
        self.leia.speak()

        self.yoda = Character()
        self.yoda.name = "Master Yoda"
        self.yoda.age = 819
        self.yoda.profession = "Jedi"
        self.yoda.speak()

        for y in self.yoda.__dict__:
        	print y

class Character():
	def __init__(self):
		#Defaykt values assigned here
		self.name = ""
		self.age = 0
		self.profession = ""

	def fight(self):
		print "YEARRGHHHHH !!!!"

	def speak(self):
		print "How do you do, my name is " + self.name

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
