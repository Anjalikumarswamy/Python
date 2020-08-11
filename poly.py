class Worker: 
    def work(self):
        print("working")

    def perform_task(self):
        print("Performing task : ", end='')
        self.work()

class Delivery(Worker):
    def work(self):
        print("Delivering Goods")

class Lumberjack(Worker):
    def work(self):
        print("Cutting Wood")


d = Delivery()
l = Lumberjack()

d.perform_task()
l.perform_task()