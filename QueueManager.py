import multiprocessing
from abc import abstractmethod
from multiprocessing import Process
from multiprocessing.managers import BaseManager


task_queue = multiprocessing.Queue()
result_queue = multiprocessing.Queue()


class QueueManager(BaseManager):
    pass


QueueManager.register("get_task_queue", callable=lambda: task_queue)
QueueManager.register("get_result_queue", callable=lambda: result_queue)


class QueueClient(Process):
    def __init__(self, port=2727, authkey=b"abc"):
        super().__init__()
        self.port = port
        self.authkey = authkey
        self.manager = None
        self.task_queue = None
        self.result_queue = None

    def connect(self):
        self.manager = QueueManager(
            address=("localhost", self.port), authkey=self.authkey
        )
        self.manager.connect()
        self.task_queue = self.manager.get_task_queue()
        self.result_queue = self.manager.get_result_queue()

    @abstractmethod
    def run(self):
        pass
