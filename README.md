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


