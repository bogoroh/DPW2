"""
Mike Taatgen
03/04/2014
Intro to Python
"""

'''
print "Hello World"
name = raw_input("Enter your name: ")
print name + ", very nice to meet you!"
'''

# Single Lined Comment

first = "Mike"

yearBorn = 1994
currentYear = 2014
age = currentYear - yearBorn
print age

# Conditionals
budget = 300
if budget > 200:
	budget += 1
	print "You can buy a pair of Jordans"
	# "pass" to skip
elif budget > 30:
	print "You can buy a pair from Payless"
else:
	print "No shoes for you!"

# Functions
def calcArea(h,w):
	a = h * w
	return a

height = 40
width = 30

area = calcArea(height, width)

# Booleans
# wonLottery = True (must be capitalized)

# Logical Operators
# "and", "or" in conditionals

# Casting
# print "Your area is:" + str(area) #int #float

# Arrays
students = ['Jairo', 'Austin', 'Bryan', 'Samantha']
students.append("Mike")

# Dictionaries
villains = dict()
villains = {"Star Wars":"Darth Vader", "Lion King":"Scar", "Silence of the Lambs":"Hannibal"}

print len(students) # "len" for length of array
print villains["Star Wars"] # prints what's inside the dictionary entry "Star Wars"

# Loops
for i in range(100,0,-1): # sets a range of 1 up to, not to include 100 "0,100,2" (even numbers)
	# print "There are " +str(i)+ " number of bottles of beer on the wall"
	pass

for s in students: # loops through arrays
	# print s + " you are the awesomest!"
	pass

# Format Method for Big Strings
your_name = "Mike"
real_age = 19
message = '''
{your_name}, thanks for joining us. This is great! You are awesome! Thumbs up!
You are {real_age} years old. That's great!
Sincerely,
	People Who Can't Spell
'''
message = message.format(**locals())
print message

# Random numbers
import random
import decimal
for y in range(0,100):
	# print random.randrange(2,9)
	print decimal.Decimal(random.randrange(300))/100