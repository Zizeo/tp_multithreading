from QueueManager import QueueClient
from task import Task
import time


class Boss(QueueClient):
    def __init__(self, num_tasks=10, size=None, port=2727, authkey=b"abc"):
        super().__init__(port=port, authkey=authkey)
        self.num_tasks = num_tasks
        self.size = size

    def run(self):
        start = time.perf_counter()
        self.connect()

        # Generate and submit tasks
        for i in range(self.num_tasks):
            task = Task(identifier=i, size=self.size)
            self.task_queue.put(task)

        # Collect results
        results = []
        for _ in range(self.num_tasks):
            result = self.result_queue.get()
            results.append(result)
            print(f"Task {result.identifier} completed in {result.time:.2f} seconds")

        end = time.perf_counter()
        print(f"Total time: {end - start:.2f} seconds")


if __name__ == "__main__":
    boss = Boss(num_tasks=10, size=500)
    boss.run()
