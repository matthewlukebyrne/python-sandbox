# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# In python you dont use semi-colons (so stop using them!)

# x = 1             # int
# y = 2.5           # float
# name = 'Matt'     # string
# is_cool = True    # bool

# Multiple assigment
x, y, name, is_cool = (1, 2.5, 'Matt', True)

# Print x without brackets works!
print(x, y, name, is_cool)

# Basic math
a = x + y

# Casting (Helping strings go with other strings)
x = str(x)
# Changes to a int
y = int(y)
# Changes to a float
z = float(y)

# Check type
print(type(z))
print(z)