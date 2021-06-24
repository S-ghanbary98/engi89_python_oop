from reptile import Reptile


class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True



# Let's add some specific Methods/behaviours

    def use_tongue_to_smell(self):
        return "If I can touch it i can smell it !!"

#Creating an objects

smart_snake = Snake()
# print(smart_snake.move())  #move() available from Animal class
# print(smart_snake.hunt())   # hunt() available from Repitle class
# print(smart_snake.use_tongue_to_smell())  # use_tongue_to_smell() available from current class


# Move onto last step