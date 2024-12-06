from QueueManager import QueueClient


class Minion(QueueClient):
    def __init__(self, port=2727, authkey=b"abc"):
        super().__init__(port=port, authkey=authkey)

    def run(self):
        self.connect()

        while True:
            try:
                # Get task from queue
                task = self.task_queue.get()

                # Process the task
                task.work()
                print(f"Task {task.identifier} running")
                # Put result back in queue
                self.result_queue.put(task)

            except Exception as e:
                print(f"Error processing task: {e}")
                break


if __name__ == "__main__":
    minion = Minion()
    minion.run()
