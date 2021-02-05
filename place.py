from move import Move
class Place:
    def __init__(self,type, werehouse, workers):
        self.__type = type
        self.werehouse = werehouse
        self.list_workers = workers
        self.changer = Move
    def new_worker(self, list_of_free_workers):
        n=0
        for person in list_of_free_workers:
            n+=1
            print(n, "  ", person.name)
        print("Choose new worker by number")
        chosen_worker = input()
        if chosen_worker in "12345":
            worker_number = int(chosen_worker)
            if worker_number < 6:
                worker_number = worker_number - 1
                print(chosen_worker)
                ja_uz_nevim =["a", "b"]
                self.changer.take_card(worker_number, ja_uz_nevim, ja_uz_nevim)
            else:
                print("This choice is invalid.")
        else:
            print("This choice is invalid.")
    def out_worker(self, whouse):
        n = 1
        print("Choose worker by number")
        for person in self.werehouse.list_of_workers:
            print(n, "  ", person.name)
        chosen_worker = input()
        print(chosen_worker)
        if chosen_worker in "12345":
            worker_number = int(chosen_worker)
            if worker_number < 6:
                self.changer.take_card(self.list_workers, whouse.list_of_workers, worker_number, worker_number)
            else:
                print("This choice is invalid.")
        else:
            print("This choice is invalid.")
    def turn(self, whouse):
        turn = True
        while turn == True:
            choice = input("If you want add person  press 1, if you want take out person  press 2, if you want end person  press 3")
            if choice == "1":
                self.new_worker(whouse)
            elif choice == "2":
                self.out_worker(whouse)
            else:
                turn = False









