from QueueManager import QueueClient


class Minion(QueueClient):
    def __init__(self, port=2727, authkey=b"abc"):
        super().__init__(port=port, authkey=authkey)
        self.running = True

    def run(self):
        self.connect()

        while self.running:
            try:
                task = self.task_queue.get(timeout=2)

                # Process the task
                task.work()
                print(f"Task {task.identifier} running")
                # Put result back in queue
                self.result_queue.put(task)

                if self.task_queue.empty():
                    self.terminate()
            except Exception as e:
                print(f"Error processing task: {e}")
                break

    def terminate(self):
        self.running = False


if __name__ == "__main__":
    minion = Minion()
    minion.run()
