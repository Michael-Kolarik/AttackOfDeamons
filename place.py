from move import Move
class Place:
    def __init__(self,type, werehouse, workers):
        self.__type = type
        self.werehouse = werehouse
        self.list_workers = workers
        self.changer = Move
    def new_worker(self):
        n = 0
        for person in self.werehouse.list_of_workers:
            n += 1
            print(n, "  ", person.name)
        print("Choose new worker by number")
        chosen_worker = input()
        if chosen_worker in "12345":
            worker_number = int(chosen_worker)
            if worker_number < 6:
                worker_number = worker_number - 1
                news = self.werehouse.choosen_worker(worker_number)
                self.list_workers.append(news)
                self.werehouse.workers_decrease(worker_number)
            else:
                print("This choice is invalid.")
        else:
            print("This choice is invalid.")
    def out_worker(self):
        n = 1
        print("Choose worker by number")
        for person in self.list_workers:
            print(n, "  ", person.name)
            n += 1
        chosen_worker = input()
        print(chosen_worker)
        if chosen_worker in "12345":
            worker_number = int(chosen_worker)
            if worker_number < 6:
                worker_number -= 1
                self.werehouse.workers_increase(self.list_workers[worker_number])
                del(self.list_workers[worker_number])
            else:
                print("This choice is invalid.")
        else:
            print("This choice is invalid.")
    def turn(self):
        turn = True
        while turn == True:
            choice = input("If you want add person  press 1, if you want take out person  press 2, if you want end person  press 3")
            if choice == "1":
                self.new_worker()
            elif choice == "2":
                self.out_worker()
            else:
                turn = False
    def work_day(self):
        if self.__type == "mine":
            for person in self.list_workers:
                person.mining()
        elif self.__type == "forest":
            for person in self.list_workers:
                person.felling()
        elif self.__type == "farm":
            for person in self.list_workers:
                person.farming()
        elif self.__type == "market":
            for person in self.list_workers:
                person.trading()
        elif self.__type == "battlefield":
            for person in self.list_workers:
                person.start_battle()
            for person in self.list_workers:
                person.battle()
            for person in self.list_workers:
                person.find_battle()






