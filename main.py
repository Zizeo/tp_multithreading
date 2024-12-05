import multiprocessing
from QueueManager import QueueManager
from Boss import Boss
from Minion import Minion
import time

"""
sur Intel® Core™ i3-8130U CPU @ 2.20GHz × 4
Pour 100 tâches :
    1 minion: 45.86s
    2 minions: 40.43s
    4 minions: 33.07s
    5 minions: 37.27s
    10 minions: 43.39s
    20 minions: 49.22s

"""


def run_manager(port=2727, authkey=b"abc"):
    manager = QueueManager(address=("localhost", port), authkey=authkey)
    server = manager.get_server()
    server.serve_forever()


if __name__ == "__main__":
    manager_process = multiprocessing.Process(target=run_manager)
    manager_process.start()

    minions = []
    start = time.perf_counter()
    for _ in range(4):
        minion = Minion()
        minions.append(minion)
        minion.start()

    boss = Boss(num_tasks=100)
    boss.start()
    boss.join()

    for minion in minions:
        minion.terminate()
    manager_process.terminate()
    end = time.perf_counter()
    print(f"Total time: {end - start:.2f} seconds")
