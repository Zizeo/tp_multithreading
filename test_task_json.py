import unittest
from task import Task
import numpy as np


class TestTaskJson(unittest.TestCase):
    def test_task_json(self):
        task = Task()
        json_str = task.to_json()
        new_task = Task.from_json(json_str)
        self.assertEqual(task, new_task)
        np.testing.assert_equal(task.a, new_task.a)
        np.testing.assert_equal(task.b, new_task.b)
        np.testing.assert_equal(task.x, new_task.x)
        new_task.work()
        np.testing.assert_allclose(np.dot(new_task.a, new_task.x), new_task.b)


if __name__ == "__main__":
    unittest.main()
