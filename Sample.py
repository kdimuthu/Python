#This is how to comment in python
print("Hello World")

#Creating Variables
x = 5
y = "John"
print("Value of y is :"+y)
print(y)

#Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# This is type funtion. It will return the type
x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

#Many Values to Multiple Variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

vehicals = ["car", "van", "bus"]
x, y, z = vehicals
print(x)
print(y)
print(z)

#Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Create a variable inside a function, with the same name as the global variable

#This is how to get the data type of a variable
a = "awesome"
print(type(a))

def myfunc():
  a = "fantastic"
  print("Python is " + a)

myfunc()

print("==Python is " + a)

#You can assign a multiline string to a variable by using three quotes.
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Strings are arrays
a = "Hello, World!"
print(a[1])

#Looping Through a String
for x in "banana":
  print(x)


#Slicing
b = "Hello, World!" 
print(b[2:5])

#Boolean Values

print(10 > 9)
print(10 == 9)
print(10 < 9)

#Evaluate a string and a number:

print(bool("Hello"))
print(bool(15))
 

   

