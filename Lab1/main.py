import random

name = raw_input("What is your name? ") #String
gname = raw_input("What's her name?") #String
friendname = raw_input("What is the name of your friend?") #String
time = int(raw_input("What time is it? (24H,Example: 1845)")) #Number
money = int(raw_input("How much money did you withdraw? Please fill in a whole number in dollars ")) #Number

#currency = float(raw_input("What is the current currency of Euro to US Dollar? (Hint=1.36) ")) #Float 

#celcius = int(raw_input("What is the weather in degrees Celcius? ")) #Number

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

food = ["Taco","Burrito","Steak Sandwich","Philly cheesesteak","Spaghetti"]
foodIndex = random.randrange(0,5)#Find out what game we are playing 
foodString = food[foodIndex] #Hold the string for the casinoGames

#nightclub 
nightclubs = {"Daytona":"Club XL","Orlando":"Vain Nightclub","Tampa":"XS Nightclub","Miami Beach":"Mansion"}
nightclub = nightclubs["Tampa"] #This will call the value


#first function calculating his new bank roll with the earnings
def bankBalance(dollar):
		balance = 6000
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
message = '''{opening} {name}. Do you remember what happend last night? You woke up at {woke}AM. Your friend {friendname} called you to ask if you wanted to go the {nightclub}. So you guys went. Since you didn't have any cash you had to go to the atm and pull out some cash. You got your receipt back and now only have {bankF}$.You entered the club and started dancing with this cute girl name {gname}. Since it was getting late you and her decided to buy something to eat before heading home. You both bought a {foodString} and decided to head to {placeF}.  '''
messageFormatted = message.format(**locals())
print messageFormatted
