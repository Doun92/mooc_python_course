# Write your solution here
# If you use the classes made in the previous exercise, copy them here
# Write your solution here:
class Task:
    id_count = 1

    def __init__(self, description:str, programmer:str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finish_status = False
        self.id = Task.id_count
        Task.id_count += 1

    def __str__(self):
        if self.finish_status == True:
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED"
        else:
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED"

    def is_finished(self):
        return self.finish_status

    def mark_finished(self):
        self.finish_status = True
        return self.finish_status

class OrderBook:
    def __init__(self):
        self.list_tasks = []

    def add_order(self, description:str, programmer:str, workload: int):
        self.list_tasks.append(Task(description,programmer,workload))
        return self.list_tasks

    def all_orders(self):
        return self.list_tasks

    def programmers(self):
        prog = list(set([task.programmer for task in self.list_tasks]))
        return prog
        
    def mark_finished(self, id: int):
        list_ids = [task.id for task in self.list_tasks]
        if id in list_ids:
            for task in self.list_tasks:
                if task.id == id:
                    task.mark_finished()
        else:
            raise ValueError("This task does not exist")


    def finished_orders(self):
        return [task for task in self.list_tasks if task.is_finished() == True]

    def unfinished_orders(self):
        return [task for task in self.list_tasks if task.is_finished() == False]

    def status_of_programmer(self, programmer: str):
        if programmer in self.programmers():
            prog_tasks = [task for task in self.list_tasks if task.programmer == programmer]

            list_finished = [t for t in prog_tasks if t.is_finished() == True]
            list_unfinished = [t for t in prog_tasks if t.is_finished() == False]

            finshed_work_hours = 0
            for t in list_finished:
                finshed_work_hours += t.workload
            
            unfinshed_work_hours = 0
            for t in list_unfinished:
                unfinshed_work_hours += t.workload

            return (len(list_finished), len(list_unfinished), finshed_work_hours, unfinshed_work_hours)
        else:
            raise ValueError("This programmer does not exist")

class OrderBookApplication:
    def __init__(self):
        self.__orderbook = OrderBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        try:
            description = input("description: ")
            prog, workload = input("programmer and workload estimate: ").split(" ")
            self.__orderbook.add_order(description, prog, int(workload))
            print("added!")
        except:
            print("erroneous input")

    def list_tasks(self, cmd):
        try:
            if cmd == "2":
                finished_tasks = self.__orderbook.finished_orders()
                if len(finished_tasks) == 0:
                    print("no finished tasks")
                else:
                    for task in finished_tasks:
                        print(task)
            elif cmd == "3":
                unfinished_tasks = self.__orderbook.unfinished_orders()
                if len(unfinished_tasks) == 0:
                    print("no finished tasks")
                else:
                    for task in unfinished_tasks:
                        print(task)
        except:
            print("erroneous input")

    def get_programmers(self):
        list_progs =  [prog for prog in self.__orderbook.programmers()]        
        for prog in list_progs:
            print(prog) 

    def mark_task_end(self):
        try:
            id_task = input("id: ")
            self.__orderbook.mark_finished(int(id_task))
            print("marked as finished")
        except:
            print("erroneous input")

    def get_status(self):
        try:
            prog = input("programmer: ")
            result = self.__orderbook.status_of_programmer(prog)
            print(f"tasks: finished {result[0]} not finished {result[1]}, hours: done {result[2]} scheduled {result[3]}")
        except:
            print("erroneous input")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_tasks(command)
            elif command == "3":
                self.list_tasks(command)
            elif command == "4":
                self.mark_task_end()
            elif command == "5":
                self.get_programmers()
            elif command == "6":
                self.get_status()
            else:
                self.help()

# if __name__ == "__main__":
application = OrderBookApplication()
application.execute()