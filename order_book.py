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

if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)