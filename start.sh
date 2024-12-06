#!/bin/bash
/home/elio/code/tp_multithreading/.venv/bin/python ./QueueManager.py&
/home/elio/code/tp_multithreading/.venv/bin/python ./Boss.py&
/home/elio/code/tp_multithreading/.venv/bin/python ./proxy.py&
