import unittest


class TestTask(unittest.TestCase):
    def test_task(self):
        import numpy as np
        from task import Task

        task = Task()
        self.assertEqual(task.identifier, 0)
        self.assertEqual(task.size, task.size)
        self.assertEqual(task.a.shape, (task.size, task.size))
        self.assertEqual(task.b.shape, (task.size,))
        self.assertEqual(task.x.shape, (task.size,))
        self.assertEqual(task.time, 0)

        task.work()

        np.testing.assert_allclose(np.dot(task.a, task.x), task.b)


if __name__ == "__main__":
    unittest.main()
