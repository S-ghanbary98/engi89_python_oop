# Pythons Documentation can be found on python.org
# We Use `import` so that we can use pthon modules available.

# Modules
import math     # To calculate values
from random import random   # To generate random values

# Pi
print(math.pi)

# Rounding figures
# If value is less than 0.5 we round down, otherwise we must round up.

num1 = 23.44        # float
print(math.ceil(num1)) # math.ceil() rounds up
print(math.floor(num1)) # math.floor() rounds down


# Random Class/Methods
print(random()) # Generates random number between 0 - 1 every time program is run


# Other Packages

import os, datetime,sys

work_dir = os.getcwd()
print(work_dir)

print(os.cpu_count())   # Returns number of cpu cores
print(os.path)          # return current pasth

print(datetime.datetime.today())    # Returns Current time
print(sys.path)                     # Returns system Path

# API Interactions
## pip is a package manager in python to intall packages that are not available.
# To install `requests package`
# `pip install requests`



import requests

requests_api = requests.get("https://www.bbc.co.uk/")

print(requests_api.status_code) # 200 for success - 404 and above
print(requests_api.headers)
print(type(requests_api.content))




