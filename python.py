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
