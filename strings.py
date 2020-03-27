# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Matt'
age = 29

# Concatenate (Join together data types with casting)
# Without cast throws a error
print('Hello I am ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position (.format)
print('{}, {}, {}'.format('a', 'b', 'c'))
# b, c, a
print('{1}, {2}, {0}'.format('a', 'b', 'c'))

# Arguments by name
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (only in 3.6+ version) prob the better way to do it (preferred)
print(f'My name is {name} and I am {age}')

# String Methods

s = 'Hello there world'


# All methods have () parentheses
# Capitalize first letter 
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length (Similar java function)
print(len(s))

# Replace
print(s.replace('world', 'lisa'))

# Count
sub = "h"
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())

