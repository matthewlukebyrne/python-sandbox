# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Will', 'Janet', 'Karen']

# Simple for loop (access in)
# for person in people:
#   print('Current person: ', person)

# Break out of loop if person is Janet (If you were to move the positioning of the break also)
# for person in people:
#   if person == 'Janet':
#     break
#   print('Current person: ', person)
  

# Continue (Skips and continues on)
# for person in people:
#   if person == 'Janet':
#     continue
#   print('Current person: ', person)

# Range (Used to loop through a specific number of times) (Kinda like a tradiontal for loop)
# for i in range(len(people)):
#   print('Current Person: ', people[i])

# for i in range(0, 11):
#   print('Number ', i)

# While loops execute a set of statements as long as a condition is true. (Very familar!)
count = 0
while count <= 10:
  print('Count: ', count)
  count = count + 1