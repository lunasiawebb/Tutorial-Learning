#multiple assignment

from sys import exception
from xml.etree.ElementPath import find


sarah = bob = mike = 17

name, age = "Lunasia", 20

#Arithmetic Operators 
age1=12
age2=18

print(age1 + age2)
print(age1 - age2)
print(age1 * age2)
print(age1 / age2)
print(age1 % age2)
print(age1 ** age2)

#strings
sentence = "Hello, my dog is cute"
print(sentence[0:5])
print(sentence)

first="lunasia" 
last="webb"
print(first + " " + last)
print("hi"*10)

#placeholders %s=string %d=integers
name="Jake"
first="Jaedin"
last="Manning"
print(name + " is a good guy.")
print("%s is a good guy." % name)

sent= "%s %s is awesome"
print(sent % ("Lunasia", "Webb"))
print("%s %s is nice" % (first, last))

#fstrings
print(f"{name} is a good guy.")
print(f"{first} {last} is awesome.")

#Excerise1
print("Exercise 1:")
x=15+30
print(x/2)

print("Exercise 2:")
x2=15
y2=30
print(x2+y2)
print(x2-y2)
print(x2*y2)
print(x2/y2)
print(x2%y2)

name="lunasia"

l,m,n= "apple", "banana", "cherry"

print("Hello " * 10)

name, age= "Lunasia", 20

sent1="Hello"
sent2="World"
sent3= sent1 + " " + sent2

sent4= "i dont like dogs" 
print(sent4[0:6])

print(sent4[0:])

#lists 
shopping_list = ["apple", "banana", "cherry"]
print(shopping_list[0:2])
shopping_list.append("blueberry")
shopping_list[0] = "grape"
del shopping_list[0]

shopping_list2 = ["milk", "bread", "eggs"]
print(shopping_list+shopping_list2)

#dictionaries
students ={'bob': 85, 'alice': 90, 'charlie': 78}
print(students['bob'])

del students["alice"]
print(len(students))

#tuples
#uses [parenthesis insead of brackets] are immuntable

tup=('oranges', 'apples', 'bananas')
print(tup[1])

names=['sarah', 'Keith', 'Mike']
sports=['soccer', 'basketball', 'tennis']
sports[1]='volleyball'

numbers=[1, 2, 3, 4, 5]
del numbers[4]
print(numbers)

num=[1,2,3]
num2=[4,5,6]
num3=num+num2
max(num3)
min(num3)
len(num3)

grades={'bob': 85, 'alice': 100, 'queen':75}
print(grades['bob'])

ages = {'garett' : 25, 'mike': 30, 'manson': 50}
del ages['mike']

print(ages)

movies = ('garfield', 'snowfall', 'toy story', 'paid in full')
print(movies[0:2])

# conditional statement
if 5>3:
    print("5 is greater than 3")

if 3<2:
    print("yo")
else:
    print("3 is not less than 2")
#elif is extra if statments after if 
#logical operators and/or

#for loops
list1= ["apple", "banana", "cherry"]
tup1=(2, 4, 6)

for item in list1:
    print(item)


for i in range(1, 11, 2):
    print(i)

for i in range(5, 51, 5):
    print(i)

# while loops
c=0
while c<5:
    c=c+1
    if c== 3:
        break #continue skips print(c) pass does nothing
    print(c)

#try and except

try:
    if name > 4:
        print("hello")
except:
    print("an error was found")


#creating a function
 # steps mix, knead, let rise, bake
 #make_special_break

def hello_world():
    print("Hello, World!")




#built in functions

abs(-23)
#bool(0) or bool(none)
#bool(1)
sent="print('hi')"
eval(sent) 
exec(sent)

print(str(10))
print(int("10"))

#classses and objects
#class dog name,breed age, behaviors
#methods barks eat sleep

#objects fido or luis
#properties

class Person :
    def __init__(self, name, age): # self is a reference to the current instance
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name
    def getAge(self):
        return self.age




p1 = Person("Bob", 21)
print(p1.getName())

#class inheritance 
class Car:
    def __init__(self):
        self.wheels=4
        self.seats=5

    def drive(self):
        print("The car is driving.")

class SportsCar(Car):
    def __init__(self):
        super().__init__()
        self.engine_power = '400 hp'
        self.seats=2 
    def drive(self):
        print("The sports car is driving.")

mySportsCar = SportsCar()


#my product of array w/ index as exception leetcode answer
def productofarray (arr):
    product_arr = []
    for i in range(len(arr)):
        product = 1
        j = 0
        while j < len(arr):
            if j != i:
                product *= arr[j]
            j += 1
        product_arr.append(product)
    return print(product_arr)    

productofarray([0, 2, 2, 2])

#the actual answer 




    

