from abc import ABC, abstractmethod
from multiprocessing import Process
from multiprocessing.managers import BaseManager


class QueueClient(ABC, BaseManager, Process):
    @abstractmethod
    def __init__(self):
        pass
