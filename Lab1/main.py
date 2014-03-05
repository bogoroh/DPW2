name = raw_input("What is your name? ") #String
time = raw_input("What day is it? ") #String
sunny = raw_input("Is it the weekend? (Yes/No) ") #String
currency = float(raw_input("What is the current currency of Euro to US Dollar? (Hint=1.36) ")) #Float 
money = int(raw_input("How much money did he find? Please fill in a whole number in Euros ")) #Number
celcius = int(raw_input("What is the weather in degrees Celcius? ")) #Number
tax = int(raw_input("How much percent do you have to pay taxes?(0-100) ")) #Number

if sunny == "Yes":
    opening = "It was a sunny"
elif :
    opening = "It was a grimy"

message = '''Good morning {name}.  '''
messageFormatted = message.format(**locals())
print messageFormatted
