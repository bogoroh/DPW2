import random

name = raw_input("What is your name? ") #String
gname = raw_input("What's her name? ") #String
friendname = raw_input("What is the name of your friend? ") #String
time = int(raw_input("What time is it? (24H,Example: 1845) ")) #Number
money = int(raw_input("How much money did you withdraw? Please fill in a whole number in dollars ")) #Number
spent = float(raw_input("How much money did you spent at the club? (Example: 123,29 ")) #Float 
days = int(raw_input("How many days? ")) #Number

if time < 1200 and time >= 600:
    opening = "Good morning"
elif time <1800:
    opening = "Good afternoon"
elif time <2400:
	opening = "Good evening"
else:
	opening = "Good night"


#Find out what time you woke up
woke = random.randrange(1,13) #randomg numbers 1,2,3,4,5,6,7,8,9,10,11,12

#Find out what food you bought
food = ["Taco","Burrito","Steak Sandwich","Philly cheesesteak","Spaghetti"]
foodIndex = random.randrange(0,5)#Find out what game we are playing 
foodString = food[foodIndex] #Hold the string for the casinoGames

#Checking which nightclub you go to 
nightclubs = dict("Daytona":"Club XL","Orlando":"Vain Nightclub","Tampa":"XS Nightclub","Miami Beach":"Mansion")
nightclub = nightclubs["Tampa"] #This will call the value


#first function calculating his new bank roll with the earnings
def bankBalance(dollar):
		balance = 12000 /2
		balance -= dollar
		return balance
bankF =  bankBalance(money)

#Second function
def place():
    bol = random.randrange(0,2)
    if bol == 1:
    	place = "her place"
    	return place
    else:
    	place = "your place"
    	return place
placeF = place()

tcolor = ""
lights = ["Red","Yellow","Green"]
for light in lights:
	tcolor = tcolor + light + ", "

message = '''{opening} {name}. Do you remember what happend last night? You woke up at {woke}AM. Your friend {friendname} called you to ask if you wanted to go the {nightclub}. The traffic light hit {tcolor}so you guys went. Since you didn't have any cash you had to go to the atm and pull out some cash. You got your receipt back and now only have {bankF}$. You entered the club and started dancing with this cute girl named {gname}. After spending {spent} at the club it was getting late you and her decided to buy something to eat before heading home. and you spent ${spent}. You both bought a {foodString} and decided to head to {placeF}. After {days} days you decided to get a tattoo with her name on it. '''
messageFormatted = message.format(**locals())
print messageFormatted
