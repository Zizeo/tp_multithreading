from QueueManager import QueueClient
from task import Task

class Boss(QueueClient):
    def __init__(self, num_tasks=10, port=2727, authkey=b'abc'):
        super().__init__(port=port, authkey=authkey)
        self.num_tasks = num_tasks
        
    def run(self):
        self.connect()
        
        # Generate and submit tasks
        for i in range(self.num_tasks):
            task = Task(identifier=i)
            self.task_queue.put(task)
            
        # Collect results
        results = []
        for _ in range(self.num_tasks):
            result = self.result_queue.get()
            results.append(result)
            print(f"Task {result.identifier} completed in {result.time:.2f} seconds")
