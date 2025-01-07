import multiprocessing
from QueueManager import QueueManager
from Boss import Boss
import time
from Minion import Minion
from proxy import run as proxy_run


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


def run_cpp():
    proxy_run()


if __name__ == "__main__":
    manager_process = multiprocessing.Process(target=run_manager)
    manager_process.start()
    boss_process = multiprocessing.Process(target=run_boss, args=(2727, b"abc"))
    boss_process.start()
    time.sleep(0.5)
    start = time.perf_counter()
    time.sleep(0.5)  # sleep pour laisser le temps au manager/boss de se lancer

    minions = []
    # minion_process = multiprocessing.Process(target=run_cpp)

    if CPP:
        minion_process = multiprocessing.Process(target=run_cpp)
        minions.append(minion_process)
        minion_process.start()
    else:
        for _ in range(MINION):
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
