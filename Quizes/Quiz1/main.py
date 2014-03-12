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

def countDown (b):
	bottles = int(b)
	for i in range(bottles, 0, -1): #bottles is the amount of beer bottles on the wall you want a range from the amount they have till 0 and subtracting 1 everytime
		if i> 1: #still grabbing beer
			message = str(i) + " Bottles of Beer on the Wall, " + str(i) +  " Bottles of Beer.. take one down and pass it around. Now you have " + str(i-1) + " bottles of beer on the wall!"
			print message
			print "----------------------------------------------"
		else: #if you are grabbing your last beer
			print "1 Bottle of beer on the wall, 1 Bottle of beer." +  "Bottles of Beer.. take one down and pass it around. Now you are out of beer and gotta call the cab"
			print "ARGHHH, I'mz a pirate that needs more beer"		

countDown(100)