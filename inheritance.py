#Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#Create a Child Class
class Student(Person):
  pass

#Add the __init__() Function
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

#Use the super() Function
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

#Add Methods
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

#This is how to import a funtion
import funtions
funtions.my_function
x=dir (funtions)
print(x)