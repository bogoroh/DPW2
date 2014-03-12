import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
		self.response.write('Hello world!')
		self.t = Transcript()
		self.t.grade1 = 90
		self.t.grade2 = 80
		self.t.quiz1 = 85
		self.t.quiz2 = 90
		self.t.calc_grade()
		self.t.final_grade += 10
		print self.t.final_grade

class Transcript(object):
	def __init__(self):
		self.grade1 = 0
		self.grade2 = 0
		self.quiz1 = 0
		self.quiz2 = 0
		self.__final_grade = 0

	# _ = protected
	# __ = Private
	# No underscore = public

	#make final_grade a property
	@property
	def final_grade(self):
	    return self.__final_grade
	@final_grade.setter
	def final_grade(self, grade):
	    self.__final_grade = grade
	


	
	def calc_grade(self):
		avg = (self.grade1 + self.grade2 + self.quiz1 + self.quiz2)/4
		self.__final_grade = avg


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
