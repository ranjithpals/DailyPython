## Import libraries
from datetime import datetime as dt
import time as t
from datetime import timedelta as td

## Define and Assign Timer Parameters
num_tasks = 4
len_task = 1
len_short_brk = 1
len_long_brk = 5

## Time Duration in terms of TimeDelta
dur_task = td(hours=len_task/60)
dur_shortbrk = td(hours=len_short_brk/60)
dur_longbrk = td(hours=len_long_brk/60)

## Current Time
curr_time = dt.now()

## Timer Logic
for i in range(num_tasks):
    print(f'Current Time: {dt.now()}')
    print(f'Task: {i+1} has started')
    task_end = curr_time + dur_task
    while dt.now() < task_end:
        t.sleep(1)
    print(f'Task: {i+1} has ended')
    print(f'Current Time: {dt.now()}')
    print('Short Break starts')
    brk_end = dt.now() + dur_shortbrk
    while dt.now() < brk_end:
        t.sleep(1)
    print('Short Break ends')
