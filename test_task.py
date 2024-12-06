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

    def test_serialization(self):
        import numpy as np
        from task import Task

        task = Task()
        json_str = task.to_json()
        new_task = Task.from_json(json_str)
        self.assertEqual(task, new_task)
        np.testing.assert_equal(task.a, new_task.a)
        np.testing.assert_equal(task.b, new_task.b)
        np.testing.assert_equal(task.x, new_task.x)
        new_task.work()
        task.work()
        np.testing.assert_allclose(np.dot(new_task.a, new_task.x), new_task.b)

        self.assertTrue(task == new_task)


if __name__ == "__main__":
    unittest.main()
