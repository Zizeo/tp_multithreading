#!/bin/bash



# Use main.py instead

NB_MINIONS=4

source .venv/bin/activate

/home/elio/code/tp_multithreading/.venv/bin/python ./QueueManager.py&
/home/elio/code/tp_multithreading/.venv/bin/python ./Boss.py&


# C++ computation
# for i in $(seq 1 $NB_MINIONS); do
#     /home/elio/code/tp_multithreading/.venv/bin/python ./proxy.py&
# done

# Python computation
# for i in $(seq 1 $NB_MINIONS); do
#     /home/elio/code/tp_multithreading/.venv/bin/python ./Minion.py&
# done
