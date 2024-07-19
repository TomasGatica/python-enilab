#   Never forget about OOP: classes, attributes and methods

#   In OOP class is a structure that allows you to group together
#   a set of properties calles attributes, and functions called mehtods to 
#   maniupalate those properties.

class Person:
    
    def __init__(self, name, age):
        self.name = name #  class variable
        self.age = age #    class variable

    def greet(self): #  class function to print greeting
        print("Hello, my name is %s" % self.name)

a = Person("Peter", 20)
b = Person("Anna", 19)

a.greet() # call a's greet method
b.greet() # call b's greet method

print(a.name)
print(a.age)
# print(Person.a) AttributeError Person object has not attribute a

print(b.name)
print(b.age)