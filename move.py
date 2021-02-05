import random
class Move:
    def __init__(self):
        self.__x = 0
    def take_card(self, index, take_pocket,  put_pocket):
        put_pocket.append(take_pocket[index])
        del(take_pocket[index])
    def take_random_card(self, take_pocket, put_pocket):
        random_card=random.randint(0,len(take_pocket)-1)
        self.take_card(random_card, take_pocket, put_pocket)

