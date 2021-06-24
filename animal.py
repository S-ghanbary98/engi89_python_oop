# Creating an animal class


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


# We need to create an object of the class in order to use the methods and attributes.

#cat = Animal()
# For cat as the user the functionality inside Animal class and method eat() is abstracted.
#print(cat.eat())
#print(cat.breath())

