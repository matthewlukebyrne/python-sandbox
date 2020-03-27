# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Tuples uses parentheses ()

# Simple tuple
fruit_tuple = ('Apple', 'Orange', 'Mango')
# Using constructor
fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))

# Get single value
print(fruit_tuple[1])

# Can not change value of tuple ordered and unchanged (hence why commented out)
# fruit_tuple[1] = 'Grape'

# Tuples with one value should have trailing comma (important) otherwise whatever is in brackets becomes a string
fruit_tuple_2 = ('Apple',)


del fruit_tuple_2

# Get length of tuple which equals 3
print(len(fruit_tuple))
 


# A Set is a collection which is unordered and unindexed. No duplicate members.

# A set uses curly braces

# Create set
fruit_set = {'Apple', 'Orange', 'Mango'}

# Check if in set (Apple is true but Apples is false, plural)
print('Apples' in fruit_set)

# Add to set
fruit_set.add('Grape')

# Remove from set
fruit_set.remove('Grape')

# Clear set (gives a empty set() )
fruit_set.clear()

# Delete set (otherwise undefined error throws)
# del fruit_set

print(fruit_set)