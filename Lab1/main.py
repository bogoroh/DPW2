name = raw_input("What is your name? ") #String
food = raw_input("What did you eat?") #String
friendname = raw_input("What is the name of your friend?") #String
time = raw_input("What time is it? (24H,Example: 1845)") #Number

currency = float(raw_input("What is the current currency of Euro to US Dollar? (Hint=1.36) ")) #Float 
money = int(raw_input("How much money did he find? Please fill in a whole number in Euros ")) #Number
celcius = int(raw_input("What is the weather in degrees Celcius? ")) #Number
tax = int(raw_input("How much percent do you have to pay taxes?(0-100) ")) #Number

if time < 1200 && time >= 600:
    opening = "Good morning"
elif time <1800:
    opening = "Good afternoon"
elif time <2400;
	opening = "Good evening"
else:
	opening = "Good night"


#
import random
#Find out what time you woke up
woke = random.randrange(1,12) #randomg numbers 1,2,3,4,5,6,7,8,9,10,11,12

message = '''{opening} {name}. Do you remember what happend last night? You woke up at {woke}AM. Your friend {friendname} called you to ask if you wanted to go the club.  '''
messageFormatted = message.format(**locals())
print messageFormatted
