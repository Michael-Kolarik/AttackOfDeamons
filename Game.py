from werehouse import Werehouse
from place import Place
from worker import Worker
my_goods = Werehouse(0,0,0,0,[])
print(my_goods.gold)
worker1 = Worker(my_goods,"worker1")
worker2 = Worker(my_goods,"worker2")
worker3 = Worker(my_goods,"worker3")
worker4 = Worker(my_goods,"worker4")
worker5 = Worker(my_goods,"worker5")
workers = []
workers.append(worker1)
workers.append(worker2)
workers.append(worker3)
my_goods.workers_increase(worker4)
my_goods.workers_increase(worker5)
location = Place ("test", my_goods, workers)

free_workers = location.list_workers
location.turn()