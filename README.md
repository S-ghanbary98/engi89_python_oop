# Python OOP
## Four Pillars of OOP
- Abstraction:
  

   Abstraction is the process of showing only essential/necessary features of an entity/object to the outside world and hide the other irrelevant information. 

- Inheritance:
  
The ability of creating a new class from an existing class. Inheritance is when an object acquires the property of another object.

- Encapsulation:
  
Encapsulation means wrapping up data and member function (Method) together into a single class.


- Polymorphism:

Polymorphism means "many forms". A subclass can define its own unique behavior and still share the same functionalities or behavior of its parent/base class.
 - Step one create an animal.py file which will contain the parent class.

```python
class Animal:       # Capital letter to follow naming convention.
    # initialise class with a built in method __init__(self)
    # self refers to current class
    def __init__(self):  # We declare our attributes in our init method
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breath(self):
        return "Keep breathing to stay alive!"

    def eat(self):
        return "Time to eat!"

    def move(self):
        return "Move left and right to stay awake"

```

 - Step two is to create a file called reptile.py to abstract data and inherit from animal.py.
   
```python
from animal import Animal

class Reptile(Animal):   # reptile class inherits methods and attributes of Animals class

    def __init__(self):
        super().__init__()   # super is used to inherit everything from parent class.
        self.cold_blooded = True
        self.tetrapods = None
        self.heart_chambers = [3, 4]


    def seek_heat(self):
        return "Looking for the sun!!"


    def hunt(self):
        return "Go hunting for food!!"


    def use_venom(self):
        return "I will use it if I have too"



# Let's create an object of the reptile class

smart_reptile = Reptile()
# print(smart_reptile.breath())  # Breath method inherited from parent class
# print(smart_reptile.hunt())     # hunt method available from Reptile class
# print(smart_reptile.eyes)
```
 - Step three is to create a file called snake.py
```
from reptile import Reptile


class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True



# Let's add some specific Methods/behaviours

    def use_tongue_to_smell(self):
        return "If I can touch it i can smell it !!"

# Creating an objects

smart_snake = Snake()
# print(smart_snake.move())  #move() available from Animal class
# print(smart_snake.hunt())   # hunt() available from Repitle class
# print(smart_snake.use_tongue_to_smell())  # use_tongue_to_smell() available from current class

```
 - step four is to create a python file that inherits the Snake class

```python
# Creating a python class

from snake import Snake


class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True



    def digest_large_prey(self):
        return "I can digest anything without chewing!!"

    def climb(self):
        return "Up we go .........."

    def __shed_skin(self):
        return "Growing out of my skin"


fast_python = Python()
print(fast_python.climb())
print(fast_python.hunt())
print(fast_python.move())
print(fast_python.lungs)
print(fast_python.use_tongue_to_smell())

```
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