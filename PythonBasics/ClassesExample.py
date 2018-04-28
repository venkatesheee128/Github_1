# Classes provide a means of bundling data and
# functionality together. Creating a new class creates
# a new type of object, allowing new instances of
# that type to be made. Each class instance can have
# attributes attached to it for maintaining its state.
# Class instances can also have methods (defined by its class)
# for modifying its state.

# Creating Classes

# class ClassName:
#    'Optional class documentation string'
#    class_suite

# The class has a documentation string,
# which can be accessed via ClassName.__doc__.
# The class_suite consists of all the
# component statements defining class members,
# data attributes and functions.


class Employee:
    # The variable empCount is a class variable whose
    # value is shared among all instances of a this class.
    # This can be accessed as Employee.empCount from inside
    # the class or outside the class.
    empCount = 0

    # The first method __init__() is a special method,
    # which is called
    # class constructor or initialization method that
    # Python calls when you create a new instance of this class.
    # self refers to the newly created object
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    # You declare other class methods like normal functions
    # with the exception that the first argument to each method
    # is self.Python adds the self argument to the list for you;
    # you do not need to include it when you call the methods.

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


# Creating Instance Objects
# To create instances of a class, you call the class
# using class name and pass in whatever arguments
# its __init__ method accepts.


emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

# Accessing Attributes
# You access the object's attributes using the dot operator
# with object. Class variable would be accessed using class name
# as follows

emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

# Instead of using the normal statements to access attributes,
# you can use the following functions −

# Returns true if 'age' attribute exists
print(hasattr(emp1, 'age'))
# If attribute does not exist, then it would be created.
setattr(emp1, 'age', 8)
# Returns value of 'age' attribute
print(getattr(emp1, 'age'))
# Delete attribute 'age'
delattr(emp1, 'age')

# Destroying Objects (Garbage Collection)
# Python deletes unneeded objects (built-in types or class
# instances) automatically to free the memory space.
# The process by which Python periodically reclaims blocks
# of memory that no longer are in use is termed
# Garbage Collection.
# Python's garbage collector runs during program execution
# and is triggered when an object's reference count
# reaches zero. An object's reference count changes as
# the number of aliases that point to it changes.
# An object's reference count increases when it is
# assigned a new name or placed in a container
# (list, tuple, or dictionary). The object's reference
# count decreases when it's deleted with del, its reference
# is reassigned, or its reference goes out of scope.
# When an object's reference count reaches zero,
# Python collects it automatically.

a = 40  # Create object <40>
b = a  # Increase ref. count  of <40>
c = [b]  # Increase ref. count  of <40>

del a  # Decrease ref. count  of <40>
b = 100  # Decrease ref. count  of <40>
c[0] = -1  # Decrease ref. count  of <40>


# You normally will not notice when the garbage collector
# destroys an orphaned instance and reclaims its space.
# But a class can implement the special method __del__(),
# called a destructor, that is invoked when the instance
# is about to be destroyed.

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")


pt1 = Point()
pt2 = pt1
pt3 = pt1
# prints the ids of the obejcts
print(id(pt1), id(pt2), id(pt3))
del pt1
del pt2
del pt3


# Class Inheritance
# Instead of starting from scratch, you can create a
# class by deriving it from a preexisting class by listing
# the parent class in parentheses after the new class name.
# The child class inherits the attributes of its parent class,
# and you can use those attributes as if they were defined
# in the child class. A child class can also override
# data members and methods from the parent.

class Parent:  # define parent class
    parentAttr = 100

    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print('Calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attribute :", Parent.parentAttr)


class Child(Parent):  # define child class
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print('Calling child method')


c = Child()  # instance of child
c.childMethod()  # child calls its method
c.parentMethod()  # calls parent's method
c.setAttr(200)  # again call parent's method
c.getAttr()  # again call parent's method

# Overriding Methods
# You can always override your parent class methods.
# One reason for overriding parent's methods is because
# you may want special or different functionality in
# your subclass.


class Parent:        # define parent class
   def myMethod(self):
      print("Calling parent method")


class Child(Parent): # define child class
   def myMethod(self):
      print('Calling child method')


c = Child()          # instance of child
c.myMethod()         # child calls overridden method

# Method Overloading
# python doesnot support method overloading

def product(a, b):
    p = a * b
    print(p)

def product(a, b, c):
    p = a * b*c
    print(p)


# Uncommenting the below line shows an error
# product(4, 5)

# This line will call the second product method
product(4, 5, 5)

# However we may use other implementation in python
# to make the same function work differently i.e.
# as per the arguments.

def add(datatype, *args):
    if datatype == 'int':
        answer = 0
    if datatype == 'str':
        answer = ''
    for x in args:
        answer = answer + x

    print(answer)


# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'Geeks')

# Data Hiding
# An object's attributes may or may not be visible outside
# the class definition. You need to name attributes
# with a double underscore prefix, and those attributes
# then are not be directly visible to outsiders.

class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
#print(counter.__secretCount)