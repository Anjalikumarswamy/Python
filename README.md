# Python
Python-Guide

Python is object-oriented high level programming language. 

Microsoft promotes Python development with IDE visual Studio Code. 

Why Python 
Simplicity 
Convenience - platform independent. 
Cross-Language operations.(#1 language)

Python Variables
A variable is a memory location where we can store values. In python, the data type will be identified according to the data we provide. 
There are two ways of assigning values to variables 
	1. Assigning a single value. Ex : a = 10, _name1 = "abc"
	2. Multiple Assignment. Ex : a=b=c=10, x,y,z = 10,20,30

Tokens : every logical line of code is broken down into components.
Keyword
Identifiers
Literals 
Operators 

Keywords - special reserved words, never to be used as variables
Ex : True, false, return 

Identifier : is the name used to identify a variable, function, class or object.
Python is case sensitive. 

Literals : raw data given to a variable. 
Ex : String, Numeric,, Boolean, Special.

Operators : are symbols that are used to carry out arithmetic and logical operations.
Various types of operators 
Arithmetic ( +,-,*,/,%,**)
Assignment (=,+=,-=,*=,/=,|=)
Comparison (==,!=, <,>,>=,<=)
Logical (and,or,not)
Bitwise (&,|, ^,<<, >>)
Identity (is, is not)
Membership (in, not in)

Data type 

Immutable - string, Numbers, Tuples
Number : int(7), float(10.5), complex (6j)
Tuples : A sequence of immutable python object. Weeks =("S","M","T", "W","T","F","S") (assignment is not possible with tuples)


#appending 5 to the tuples - will fail because it cannot be changes.
#AttributeError: 'tuple' object has no attribute 'append'
nums.append(5)
print(nums)

Mutable - Dictionaries, List, Sets
List - A sequence of mutable objects, similar to tuples but can add dynamic data. Week = ['S","M","T"], mixed = [1, 1.5, 'a',[1,3],(1,30)]

Dictionaries : An unordered collection of items, we can create key value pair.
Sal ={"A" : 1, "B":2}

Set: An unordered collection of immutable data which has no duplicate elements




Functions : A block of organized, reusable set of instructions that is used to perform some related actions
User defined and built-in functions

Def func_name (arg1, arg2,arg3…)
--Stmt--
--return(expression)

Lambda expression : a function having no name, it cannot contain more than one expression.
Synatx: 
Lamda arguments : expression
X = lambda a : a+ 10
Print(x(5)


Array - used to store multiple values in a single variable, python doesn’t have built in arrays, but list can be used.
Cars =["ford","BWM","audi"]

Accessing an element 
X = cars[0] 
-Ford 

Modifying an element 
Cars[0] ="Honda"
Print(cars[0])
-Honda

Length of the array
X = len(cars)

Adding an element 
Cars.append("Ferrari")
Print(len(cars))

Removing an element from a position
Cars.pop(1)

Cars.remove("bmw")

File Handling 
	- Is important in any application that handles permanent data.
	- We will need file handling if we have to read from or write to files.
	- Open()
	- 'r'- read 
	- 'a'- append
	- 'w'-write
	- 'x'-create
	- Read()
	- Remove()


Python Classes and Objects

Python is an object-oriented programming language

Object-oriented programming - is a programming paradigm where you can use a real world entity which is an object.

Almost everything in python is an object, with its properties and methods
Class is like blueprint for creating objects.
Objects are defined and created from the classes.
Method - Regular Function that are part of the class
Attributes -  Variables that hold data that are a part of the class
Objects -  A specific instance of a class.


Class : 
Syntax
  Class NameOfClass:
        stmts

Object :
Syntax 
    <obj-name> = NameOfClass()

To access the class member, we use dot operator.
__init__ is a special method in python classes is a constructor method for a class
It is also called whenever an object of the class is constructed. 

Inheritance in Python : 
One class is acquiring the property of another class. 

Different types of Inheritance in Python 
Single - single class inherits from a class
Multiple - A class inherits from multiple classes.
Multi-level - One class inherits from a class, which will inherit from another class.
Hierarchical - more than one class inherit from a class
Hybrid - combination of any two kinds of inheritance.


Inheritance Super function - used to call a method from parent class.

Overriding Vs Overloading
Overloading - same function with different parameters.
Overriding - subclass may change the functionality of a python method in the superclass.


Encapsulation : Abstraction + Data hiding. Abstraction is showing essential features and hiding non-essential features to the users. 

Private method -  function would start with __
x: __add()
To change the value of the a private variable, a setter method is used.


Polymorphism:
Functions with same name, but functioning in different ways


Module 
A file containing python code.
A module can be define function, classes and variables and also include runnable code.
There are pre-defined modules in python standard library.

Keyword - from - allows you to specify the things that you want to import from a module.
From utils import add,substract

Import - import command allows you to import the complete module.
Ex : import os

Python Standard library is very extensive and offers a wide range of facilities.

Installing packages - you can use pip
Pip install <packageName>


Exception Handling : An exception is a runtime error caused by things that are outside the developer control. 
FileNotFoundException 

Try - try allows you to define a code block that could throw an exception.
Except - allows you define a code block when an exception is raised.
Finally- code block that gets run even if an exception is thrown or not.
Raise - allows you to raise your own custom exception

