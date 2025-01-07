# Projet de Multithreading

Ce projet implémente un système de traitement de tâches en utilisant le multithreading avec Python. Il utilise des minions pour exécuter des tâches en parallèle, gérées par un boss.

## Structure du Projet

- [main.py](cci:7://file:///home/elio/code/tp_multithreading/main.py:0:0-0:0): Point d'entrée du programme qui démarre le gestionnaire et les minions.
- [Boss.py](cci:7://file:///home/elio/code/tp_multithreading/Boss.py:0:0-0:0): Classe qui gère la création et l'envoi de tâches aux minions.
- [Minion.py](cci:7://file:///home/elio/code/tp_multithreading/Minion.py:0:0-0:0): Classe représentant un minion qui exécute les tâches.
- [QueueManager.py](cci:7://file:///home/elio/code/tp_multithreading/QueueManager.py:0:0-0:0): Gère les files d'attente pour les tâches et les résultats.
- [task.py](cci:7://file:///home/elio/code/tp_multithreading/task.py:0:0-0:0): Définit la classe [Task](cci:2://file:///home/elio/code/tp_multithreading/task.py:6:0-53:9) qui représente une tâche à exécuter.
- [start.sh](cci:7://file:///home/elio/code/tp_multithreading/start.sh:0:0-0:0): Script pour démarrer le projet.
- [README.md](cci:7://file:///home/elio/code/tp_multithreading/README.md:0:0-0:0): Documentation du projet.

## Installation

Python 3.10 ou plus est requis.
Utilisez uv et Cmake pour build le projet.

```bash
pip install uv
uv venv
uv sync
uv run main.py
```
