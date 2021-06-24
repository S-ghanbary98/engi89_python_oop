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