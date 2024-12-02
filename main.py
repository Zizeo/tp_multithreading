import multiprocessing
from QueueManager import QueueManager
from Boss import Boss
from Minion import Minion


def run_manager(port=2727, authkey=b"abc"):
    manager = QueueManager(address=("localhost", port), authkey=authkey)
    server = manager.get_server()
    server.serve_forever()


if __name__ == "__main__":
    manager_process = multiprocessing.Process(target=run_manager)
    manager_process.start()

    minions = []
    for _ in range(10):
        minion = Minion()
        minions.append(minion)
        minion.start()

    boss = Boss(num_tasks=60)
    boss.start()
    boss.join()

    for minion in minions:
        minion.terminate()
    manager_process.terminate()
