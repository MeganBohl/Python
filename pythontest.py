msg = "Hello World"
print msg

#CONDITIONALS
    #IF
x=4
if x<6:
    print("this is true")

x=7

    #ELIF
color = "purple"
if color == "red":
    print ("color is red")
elif color == "blue":
    print ("blue")
else:
    print ("color isn't red or blue")

#LOGICAL OPERATORS

if color == "red" and x <10:
    print ("color is red and x is less than 10")


    #FOR LOOP
people = ["John,Sarah,Tim,Bob"]
for person in people:
    print('current person:',person)

    #iterate by seq index    
     #i= iteration
for i in range (len(people)):
    print('current person:',people[i])

for i in range (0,10):
    print(i)
## Prints 0-9, iterates by 1 from 0-10

        #WHILE LOOP
count = 0
while count < 10:
    print ("count:",count)
    count = count+1
#counts by 1, from 0, up to 10    

    #FUNCTIONS
            #def=define
def sayHello():
    print('Hello')
sayHello()

    #Return a value
def getSum(num1,num2):
    total = num1 + num2
    return total

numSum=getSum(1,2)
print(numSum)

        #immutable...initial function will not be updated
def addOneToNum(num):
    num = num + 1
    print('Value inside function: ', num)
    return

num = 5
addOneToNum(num)
print('Value outside function: ', num)

        #mutable...can be updated (added 4 to list)
def addOneToList(myList):
    myList.append(4)
    print('value inside function:', myList)
    return
    
myList  = [1,2,3]
addOneToList(myList)
print('Value outside function:', myList)

    #STRING FUNCTIONS

myStr="Hello World"
print (myStr.capitalize())

print (myStr.center)

print (myStr.replace('World', 'Devops'))