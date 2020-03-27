# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
  # Constructor
  # __init__ 
  # In python the "this" keyword for class is now "self"
  # self needs to be also passed into the constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age

  def greeting(self):
    return f'My name is {self.name} and I am {self.age}'
  
  def has_birthday(self):
    self.age += 1

# Customer class (Extends the above constructor and class of user)
class Customer(User):
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0

  def set_balance(self, balance):
    self.balance = balance

  def greeting(self):
    return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}'

# Init user object above at the top
matt = User('Matt Byrne', 'matt@gmail.com', 29)
janet = User('Janet Williams', 'janet@gmail.com', 27)

# Edit property
matt.age = 38

janet.has_birthday()

# Call method (Methods have to have parentheses / brackets)
print(janet.greeting())

# Init customer
john = Customer('John Doe', 'john@gmail.com', 40)

john.set_balance(500)

print(john.greeting())