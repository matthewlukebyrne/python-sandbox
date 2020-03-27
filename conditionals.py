# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 10

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
# Standard Stuff

# Simple if
# Use of F-String (format examples)
# Will return nothing to console if not true
# if x == y:
#   print(f'{x} is equal to {y}')

# # If/else
# if x > y:
#   print(f'{x} is greater than {y}')
# else:
#   print(f'{x} is less than {y}')



  
# elif
# if x > y:
#   print(f'{x} is greater than {y}')
# Else if operators (other options)
# elif x == y:
#   print(f'{x} is equal to {y}')  
# else:
#   print(f'{x} is less than {y}')



# Nested if (Not used much better option below with logical operators)
# if x > 2:
#   if x <= 11:
#     print(f'{x} is less than 2 and greater than 10')
    

# Logical operators (and, or, not) - Used to combine conditional statements

# and (Both have to)
# if x > 2 and x <=10:
#   print(f'{x} is less than 2 and greater than 10')

# # or (Only one has to match)
# if x > 2 or x <=10:
#   print(f'{x} is less than 2 or greater than 10')

# # not 
# if not(x == y):
#   print(f'{x} is not equal to {y}')


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

# numbers = [1,2,3,4,5]

# in (Returns nothing if false)
# if x in numbers:
#   print(x in numbers)

# not in
# if x not in numbers:
#   print(x in numbers)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
# if x is y:
#   print(x is y)


# is not
# if x is not y:
#   print(x is not y)