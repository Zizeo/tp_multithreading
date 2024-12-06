import time

import numpy as np
import json


class Task:
    def __init__(self, identifier=0, size=None):
        self.identifier = identifier
        # choosee the size of the problem
        self.size = size or np.random.randint(300, 3_000)
        self.size = int(self.size)
        # Generate the input of the problem
        self.a = np.random.rand(self.size, self.size)
        self.b = np.random.rand(self.size)
        # prepare room for the results
        self.x = np.zeros((self.size))
        self.time = 0

    def work(self):
        start = time.perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        self.time = time.perf_counter() - start

    def to_json(self):
        return json.dumps(
            {
                "identifier": self.identifier,
                "size": self.size,
                "a": self.a.tolist(),
                "b": self.b.tolist(),
                "x": self.x.tolist(),
                "time": self.time,
            }
        )

    @classmethod
    def from_json(cls, json_str) -> "Task":
        data = json.loads(json_str)
        task = cls(data["identifier"], data["size"])
        task.time = float(data["time"])
        task.a = np.array(data["a"])
        task.b = np.array(data["b"])
        task.x = np.array(data["x"])
        return task

    def __eq__(self, other):
        return (
            self.identifier == other.identifier
            and self.size == other.size
            and np.allclose(self.a, other.a)
            and np.allclose(self.b, other.b)
            and np.allclose(self.x, other.x)
        )
