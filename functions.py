# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create function
def sayHello(name):
  """
  Prints Hello and then Name (This is a docstring)
  """
  print('Hello ' + name)
# Call and indent out
sayHello('Sam')



# Return Value
def getSum(num1, num2):
  """
  Definition of scope also valid in python functions
  """
  total = num1 + num2
  return total
# Indent out and print
numSum = getSum(2,3)
print(numSum)



# Another Function value
def addOneToNum(num):
  """
  sets up the +2 and then adds outside indentation
  to equal 8
  """
  num += 2
  return num
num = 6
new_num = addOneToNum(num)
print(new_num)




# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions


# Dont need a return
getSum = lambda num1, num2 : num1 + num2
print(getSum(9 , 2))

# Totals 7
addOneToNum = lambda num : num + 1
print(addOneToNum(6))