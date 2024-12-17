import multiprocessing
from QueueManager import QueueManager
from Boss import Boss
import time
from Minion import Minion
from proxy import Proxy

"""
sur Intel® Core™ i3-8130U CPU @ 2.20GHz × 4
Pour 100 tâches taille 1000 :
    1 minion: 45.86s
    2 minions: 40.43s
    4 minions: 33.07s
    5 minions: 37.27s
    10 minions: 43.39s
    20 minions: 49.22s

"""
MINION = 4
CPP = True


def run_manager(port=2727, authkey=b"abc"):
    manager = QueueManager(address=("localhost", port), authkey=authkey)
    server = manager.get_server()
    server.serve_forever()


def run_boss(port=2727, authkey=b"abc"):
    boss = Boss(num_tasks=100, size=1000, port=port, authkey=authkey)
    boss.run()


def run_minion(port=2727, authkey=b"abc"):
    minion = Minion(port=port, authkey=authkey)
    minion.run()


def run_cpp(port=2727, authkey=b"abc"):
    proxy = Proxy()
    proxy.run()


if __name__ == "__main__":
    manager_process = multiprocessing.Process(target=run_manager)
    manager_process.start()
    boss_process = multiprocessing.Process(target=run_boss, args=(2727, b"abc"))
    boss_process.start()
    time.sleep(0.5)
    start = time.perf_counter()
    time.sleep(0.5)  # sleep pour laisser le temps au manager/boss de se lancer

    minions = []
    for _ in range(MINION):
        if CPP:
            minion_process = multiprocessing.Process(target=run_cpp, args=(8000,))
        else:
            minion_process = multiprocessing.Process(
                target=run_minion, args=(2727, b"abc")
            )
        minions.append(minion_process)
        minion_process.start()

    for minion in minions:
        minion.join()

    for minion in minions:
        minion.terminate()
    manager_process.terminate()
    boss_process.terminate()
    end = time.perf_counter()
    print(f"Total time: {end - start:.2f} seconds")
