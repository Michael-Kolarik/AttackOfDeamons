class Werehouse:
    def __init__(self, wood, iron, food, gold, workers):

        self.wood = wood
        self.iron = iron
        self.food = food
        self.gold = gold
        self.list_of_workers = workers

    def wood_incerease(self, much):
            self.wood += much

    def wood_decrease(self, much):
        self.wood -= much

    def iron_incerease(self, much):
            self.wood += much

    def iron_decrease(self, much):
        self.wood -= much

    def food_incerease(self, much):
            self.wood += much

    def food_decrease(self, much):
            self.wood -= much

    def gold_incerease(self, much):
            self.wood += much

    def gold_decrease(self, much):
        self.wood -= much

    def gold(self):
        return self.gold

    def workers_increase(self, worker):
        self.list_of_workers.append(worker)

    def workers_decrease(self, index):
        del self.list_of_workers[index]

    def choosen_worker(self, index):
        return self.list_of_workers[index]
