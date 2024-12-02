from abc import ABC, abstractmethod
from multiprocessing import Process, Queue
from multiprocessing.managers import BaseManager
from task import Task

class QueueClient(ABC, BaseManager, Process):

    @abstractmethod
    def __init__(self):
        pass





