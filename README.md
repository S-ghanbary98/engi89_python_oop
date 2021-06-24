# Python OOP
## Four Pillars of OOP


## Creating Functions

- The syntax used to declare a function is `def` then the name of the function():
- We can Call a function using the function name.

#### First Iteration


```
def greeting():
    print("Welcome on Board! enjoy your trip")
    
greeting()
```




#### Second Iteration: adding a return statement
```
def greeting():
    return "Welcome on Board! enjoy your trip"

print(greeting()) # prints the return statement of the function.
```

#### Third Iteration: Passing arguments to functions.

```
def greeting(name):
#   print(name)
    return "Welcome on board!! " + name

print(greeting("shervin"))
```

#### Fourth Iteration: Prompt user to enter their name and display it back by running it through a function.

```

def greeting():
    name = input("What is your name?")
    return "welcome on board " + name

print(greeting())
```


#### Fifth Iteration: Multiple Arguments and Using Integers

##### Addition Function:
```
def add(num1, num2):
    print("This function adds two numbers together")
    return num1 + num2

print(add(9, 3))
```
##### Multiplication Function:
```
def multiply(num1, num2):
    print("This function multiplies two numbers together")
    return num1 * num2

print(multiply(9,3))
```

## Python Modules, Packages and Libraries
import math     # To calculate values
from random import random   # To generate random values

### Pi

`print(math.pi)`

### Rounding figures

- If value is less than 0.5 we round down, otherwise we must round up.

```
num1 = 23.44        # float
print(math.ceil(num1)) # math.ceil() rounds up
print(math.floor(num1)) # math.floor() rounds down
```

### Random Class/Methods

- `random()` generates random number between 0 - 1 every time program is run
```
print(random())
```


## Other Packages
```
import os, datetime, sys

work_dir = os.getcwd()  #returns current path
print(work_dir)

print(os.cpu_count())   # Returns number of cpu cores
print(os.path)          # return current pasth

print(datetime.datetime.today())    # Returns Current time
print(sys.path)                     # Returns system Path
```



## API Interactions

-pip is a package manager in python to intall packages that are not available.
- To install the `requests package` the following must be typed in the terminal.

`pip install requests`

### First API Request: BBC News

```
import requests

requests_api = requests.get("https://www.bbc.co.uk/")

print(requests_api.status_code) # 200 for success - 404 and above
print(requests_api.headers)
print(type(requests_api.content))

```