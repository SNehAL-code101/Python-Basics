#!/usr/bin/env python
# coding: utf-8

# In[86]:


#Printing 1st program
print("Hello snehal")


# # 1. DATATYPES

# In[2]:


#Integer
print(123)


# In[3]:


#float
floating_num = 345.56
print(floating_num)
type(floating_num)


# In[5]:


#oolean
isTrue = True
type(isTrue)


# In[7]:


#String
print("Snehal Rajapurkar")


# In[11]:


#List - [] MUTABLE
myLit = [1,23,23.2,258]
print(myLit)
type(myLit)


# In[12]:


#value can e changed
myLit[2] = 89
myLit


# In[14]:


#Tuple - () IMMUTABLE
myTuple = (12,25,85,56)
myTuple


# In[48]:


#value cannot e changed
myTuple[1] = 56
myTuple


# In[17]:


#SET - {} . IMMUTABLE, cannot have duplicate value like TUPLE
myet = {25,56,58, 59, 56}
print(myet)
type(myet)


# In[21]:


#DICTIONARIES - {}, key value pairing
myDict = {
    "name": "Snehal",
    "age": 25
}

print(myDict["name"])


# # 2.LISTS

# In[8]:


#Create
veggie = ["bhindi", "Cabbage", "Beans", "Carrot"]
veggie


# In[9]:


#Read
print(veggie)


# In[10]:


# Indexing
print(veggie[1])
print(veggie[-1])


# In[11]:


#Update
veggie[2] = 'pea'
veggie


# In[12]:


veggie.append("Potato")
print(veggie)


# In[13]:


veggie.insert(0, "Tomato")
veggie


# In[14]:


#Delete
del veggie[-1]


# In[15]:


veggie


# # 3.Dictionaries

# In[16]:


#CREATE
myDict = {
    "name": "Snehal",
    "age": 25,
    "Hobby": "Dance"
}


# In[17]:


#READ
myDict


# In[20]:


myDict["name"]


# In[21]:


myDict.keys()


# In[23]:


myDict.values()


# In[22]:


myDict.items()


# In[25]:


#UPDATE
myDict["name"] = "Rani"
myDict


# In[26]:


myDict["allergy"] = "AC"
myDict


# In[27]:


#DELETE
del myDict["allergy"]


# In[28]:


myDict


# # 4.CONDITIONS AND LOGIC

# In[1]:


#if tatement 
name = "Rani"
if name == "Rani":
    print("Hello " + name)


# In[3]:


#if..elif..else tatement 
mark = 50
if mark > 50:
    print("mark is greater than 50")
elif mark <50:
    print("mark less than 50")
else:
    print("mark is 50")


# In[29]:


#Create lit
veggie = ["bhindi", "Cabbage", "Beans", "Carrot"]
if "Carrot" in veggie:
    print("Hey Carrot")


# # 5.LOOPS

# In[9]:


#for loop with break statement
for veggie_name in veggie:
    if veggie_name == "Beans":
        print("I love Beans\n")
        break
    else:
        print(veggie_name + " is my Average veggie \n")


# In[10]:


#for loop with continue statement
for veggie_name in veggie:
    if veggie_name == "Beans":
        print("I love Beans\n")
        continue
    else:
        print(veggie_name + " is my Average veggie \n")


# In[13]:


#loop x numer of time
for x in range(11, 21):
    print(x)


# In[18]:


#while loop with String formatting
launch_shuttle = 0
total_shuttle = 5
while True:
    print("shuttle {} Launched".format(launch_shuttle+1))
    launch_shuttle += 1
    if launch_shuttle == total_shuttle:
        print("all {} shuttle launched".format(total_shuttle))
        break


# In[19]:


#CREATE
myDict = {
    "name": "Snehal",
    "age": 25,
    "Hobby": "Dance"
}
for key in myDict.keys():
    print(key)


# In[20]:


for value in myDict.values():
    print(value)


# In[24]:


myDict.items()


# In[25]:


for key, value in myDict.items():
    print(key, value)


# In[31]:


#Lit comprehenion
new_Lit = [veggie_name.title() for veggie_name in veggie]


# In[32]:


new_Lit


# # 6.FUNCTIONS

# In[33]:


#defining function 
def myFunc():
    print("my function")


# In[34]:


#calling a function
myFunc()


# In[35]:


names = ["neil armstrong", "buzz aldrin", "sally ride", "yuri gagarin", "elon musk"]


# In[39]:


#Positional Arguments
def custom_welcome(name):
    print("Welcome {}".format(name))


# In[40]:


custom_welcome("Rani")


# In[41]:


for name in names:
    custom_welcome(name)


# In[42]:


#Multiple Positional Arguments
def custom_welcome_to_ship(name, spaceship):
    print("Welcome {} to the {}".format(name, spaceship))


# In[44]:


custom_welcome_to_ship("Nick Renotte", "Galatic 1")


# In[45]:


spaceship = ["Galatic 1", "Galatic 2", "USS Voyager", "WOW", "Apple"]


# In[46]:


spaceship[2]


# In[47]:


for idx,name in enumerate(names):
    ship = spaceship[idx]
    custom_welcome_to_ship(name, ship)


# In[51]:


#This is uing keyword arguement
def space_suit(color ="Red"):
    print("Your space suit is {} in color".format(color))


# In[52]:


space_suit("Blue")


# In[61]:


#Multiple keyword argument
def space_suit_welcome(name, spaceship, color="Red", allergy="None"):
    print("Welcome {} to the {}, your space suit is {} in color and you have {} allergy".format(name, spaceship,color,allergy))


# In[62]:


for idx,name in enumerate(names):
    ship = spaceship[idx]
    space_suit_welcome(name, ship, "Maroon")


# In[64]:


space_suit_welcome(name, ship, "Maroon", "Peanut" )


# In[65]:


#return statement
def space_suit_welcome_with_return(name, spaceship, color="Red", allergy="None"):
    return "Welcome {} to the {}, your space suit is {} in color and you have {} allergy".format(name, spaceship,color,allergy)


# In[66]:


#Example of storing result inside of variale to use it later
welcome = space_suit_welcome_with_return(name, ship, "Maroon", "Peanut" )
print(welcome)


# In[68]:


#Lambda function
pi = lambda x: x*3.14


# In[69]:


pi(3)


# # 7.CLASSES

# In[78]:


#classes as boilerplates for object
class Person():
    #this is a method that runs as soon as you create a class, - initialise
    def __init__(self, name, age, color):
        #Create some attribute for our Person class
        self.name = name
        self.age = age
        self.color = color

    #Date of birth method
    def yob(self):
        return 2025-self.age

    #Projected age
    def project_age(self, years=5):
        return self.age + years


# In[79]:


new_Person = Person("Rani", 25, "White")


# In[80]:


#Accessing a class attribute
new_Person.color


# In[81]:


#Run a method
new_Person.yob()


# In[84]:


#Run a method with keyword argument
new_Person.project_age(10)


# ## 8.INHERITANCE -
# - PARENT is a class passing down attributes and methods = PERSON
# - CHILD is a class inheriting the methods and attributes = ASTRONAUT

# In[103]:


#create a Child class
class Astronuat(Person):

    #Define initilization function
    def __init__(self, name, age, color, duration_in_month):
        #this is what gives us inheritance - SUPER METHOD
        super().__init__(name, age, color)
        self.duration_in_month = duration_in_month

    def age_on_return(self):
        return self.project_age(years= int(self.duration_in_month/12))


# In[104]:


new_astronuat = Astronuat('Nick', 99, 'purple', 8)


# In[105]:


#Accessing parent like attribute
new_astronuat.name


# In[106]:


#Accessing parent method
new_astronuat.yob()


# In[107]:


new_astronuat.age_on_return()


# # 9.MODULES

# In[46]:


#import launch code helper
from helpers import launch_codes


# In[47]:


launch_codes()


# # 10. Working with Packages

# In[ ]:


pip install requests


# In[ ]:


pip list


# In[117]:


import requests


# In[118]:


#get documentation
get_ipython().run_line_magic('pinfo2', 'requests.get')


# In[150]:


#I can haz dad joke api endpoint
joke_url = 'https://icanhazdadjoke.com'

#iss api endpoint
iss_url = 'https://api.wheretheiss.at/v1/satellites/25544'


# In[151]:


#this is setting up header - Metadata for api request
my_header = {'Accept': 'application/json'}

#API call
results = requests.get(joke_url, headers=my_header)


# In[152]:


#Extract JSon result from API
joke = results.json()


# In[153]:


type(joke)


# In[154]:


joke['joke']


# In[155]:


#making ISS API call
iss_results = requests.get(iss_url, headers=my_header)


# In[156]:


#Statu of the api req
iss_results


# In[157]:


#Extract JSon reult from API
iss_results.json()


# # 11. Working with Files

# In[4]:


# Write out our mission journal
with open("mission_journal.txt", 'w') as f:
    f.write("It's my first day on the space mission. It is very nice")


# In[6]:


#Read from journal
with open("mission_journal.txt", 'r') as f:
    file = f.read()


# In[7]:


file


# # 12.Error Handling

# In[9]:


# Create a set
new_set = {1,2,3,5,6,7}


# In[12]:


#try something uing try keyword
try:
    #run piece of code which may cause error
    new_set[3] = 56
#If we have error, this code will run
except Exception as e:
    #print(e)
    #print out Something that is little nicer for the user
    print("Something went wrong with your req")


# # 13. MATH

# In[13]:


# Create 2 variables
math_value1= 1235
math_value2 = 5879


# In[14]:


math_value1


# In[36]:


#Addition
math_value1 + math_value2


# In[37]:


#Subtraction
math_value1 - math_value2


# In[38]:


#Multiplication
math_value1 * math_value2


# In[39]:


#Division
math_value1 / math_value2


# In[40]:


#Division with Integral Result
math_value2 // math_value1


# In[41]:


#Modulus
math_value2 % math_value1


# In[42]:


#Power
math_value2 ** 2


# In[43]:


#Round a value with specified decimal places
round(123566.22255555,2)


# In[44]:


#Absolute values takes any value and gives poitive result
abs(-56)


# In[30]:


#Minimum 
min(5,9)


# In[32]:


#Maximum
max(45,98,90,0,23)


# In[33]:


#Import MATH package
import math


# In[35]:


int(math.sqrt(25))


# In[ ]:




