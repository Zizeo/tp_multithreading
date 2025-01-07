import multiprocessing
from abc import abstractmethod
from multiprocessing.managers import BaseManager


task_queue = multiprocessing.Queue()
result_queue = multiprocessing.Queue()


class QueueManager(BaseManager):
    pass


QueueManager.register("get_task_queue", callable=lambda: task_queue)
QueueManager.register("get_result_queue", callable=lambda: result_queue)


class QueueClient:
    def __init__(self, port=2727, authkey=b"abc"):
        self.port = port
        self.authkey = authkey
        self.manager = None
        self.task_queue = None
        self.result_queue = None
        self.connect()

    def connect(self):
        self.manager = QueueManager(address=("", self.port), authkey=self.authkey)
        try:
            self.manager.connect()
        except ConnectionRefusedError:
            print("Connection to the manager failed. Is it running?")
            raise
        self.task_queue = self.manager.get_task_queue()
        self.result_queue = self.manager.get_result_queue()

    @abstractmethod
    def run(self):
        pass


if __name__ == "__main__":
    manager = QueueManager(address=("", 2727), authkey=b"abc")
    server = manager.get_server()
    server.serve_forever()
