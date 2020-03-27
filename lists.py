# A List is a collection which is ordered and changeable. Allows duplicate members.

# A list is essenitally a array in python! [] square brackets

# Create list (Mosy Common Way)
numbers = [1,2,3,4,5]
# Using a constructor (Used but not as much as the first)
numbers = list((1,2,3,4,5))

# Another List
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Get value
print(fruits[1])

# Get len (Gets the amount which is 4)
print(len(fruits))

# Append to list (Mangos added)
fruits.append('Mangos')

# Remove from list (Gets rid of grapes)
fruits.remove('Grapes')

# Insert into position (insert into position of array)
fruits.insert(2, 'Strawberries')

# Remove from position
fruits.pop(3)

# Reverse list 
fruits.reverse()

# Sort list (Alpahabetical)
fruits.sort()

# Reverse sort (Reverse Alphabetical)
fruits.sort(reverse=True)

print(fruits)