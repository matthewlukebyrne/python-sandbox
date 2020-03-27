# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules (Handy Imports)
import datetime
import time
from datetime import date
from time import time

# Pip modules (Pip Package Manager is where its at, used pip3 to simply install camelcase)
import camelcase

# Custom modules
import validator
# import validate email
from validator import validate_email

# today = datetime.date.today()
today = date.today()
timestamp = time()

camel = camelcase.CamelCase()
text = 'hello there world'
# print with a method called hump which will then in turn make every word of hello there world camelcase
print(camel.hump(text))

# Custom Modules (from validator.py) Sample Email Validation
email = 'test@test.com'
if validate_email(email):
  print('Email is valid')
else:
  print('Not a Email')