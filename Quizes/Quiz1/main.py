# Mike Taatgen
# 03-11-14
# DPW2
# Quiz 1


class CalcArea():
	def calcArea (w,h):
		area = str(w * h) #Stringify the area

		if (w == h): #check if the are identical
			print "The area of your square is " + area + " square feet."
		else: # If they are not identical
			print "The area of your rectangle is " + area + " square feet."
			
	area = calcArea(40,20)



