#Concatenation

first_name = 'Megan'
last_name = 'Bohl'
full_name = first_name + ' ' + last_name

print (full_name)

# Make List

States = ['CA','FL','NY','WA']
first_state = States[0]  #first item in list
last_state = States[-1]  #last item in list

bikes = ['trek', 'redline', 'giant']
first_bike = bikes[0]
last_bike = bikes[-1]

print first_state  
print last_state

# loop through list

for state in States:
    print (state)

#add items to list
States = []
States.append('VA')
States.append('AZ')
States.append('OK')

print States

#numerical lists
squares = []
for x in range(1,11):
    squares.append(x**2)

print squares

#slicing a list
finishers = ['Megan', 'Chris', 'Joe', 'Bob']
first_two = finishers[:2]

print first_two

#making a tuple  (sequence of immutable objects. uses parentheses instead of brackets). Even if tuple contains only one item, comma is needed tup1 = (50,);

dimensions = (1920,1080)

print dimensions

age = 16 
if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 10
else:
    ticket_price = 15

print ticket_price

#simple dictionary (key/value pair series separated by commas)
alien = {'color':'green', 'points':5}

print {"the aliens color is " + alien['color']}

alien['x_position'] = 0 #add a new key-value pair

print alien

#looping through all key-value pairs

fav_numbers = {'eric': 17, 'ever':4, 'Bob': 16}
for name,number in fav_numbers.items():
    print(name+ ' loves '+ str(number))

#looping through all keys
for name in fav_numbers.keys():
    print(name + ' loves a number')

#looping through all the values
for number in fav_numbers.values():
   print((str)(number) + ' is a favorite')

#prompting for a value

name = raw_input("What's your name? ")  #use raw_input instead of input for Python <3
print str("Hi there, " + name + "!")


age = input("How old are you? ")
age = int(age)
print age

pi = input("what's the value of pi?")
pi = float(pi)
print pi
    

    




