class Person:
      def __init__(self, name, age): # Person's constructor
          self.name = name # Person's attribute
          self.age = age # Person's attribute

      def greet(self): # Person's method
          print("Hello, my name is %s!" % self.name)

class TenYearOldPerson(Person): # TenYearOldPerson inherits from Person

      def __init__(self, name): # TenYearOldPerson's constructor
          Person.__init__(self, name, 10) # accesses Person's constructor

      def greet1(self): # rewrites the greet method
          print("I don't talk to strangers!!")

tyo = TenYearOldPerson("Jack") # instance of TenYearOldPerson
tyo.greet()
tyo.greet1() # call greet method of the TenYearOldPerson