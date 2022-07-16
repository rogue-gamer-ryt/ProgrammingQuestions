"""
Design an algorithm that takes as input a set of tasks and retums an optimum assignment.
"""
import collections
PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))

def optimum_task_assignment(task_durations):
    task_durations.sort()
    return [
        PairedTasks(task_durations[i], task_durations[~i])
        for i in range(len(task_durations) // 2)
    ]

print(optimum_task_assignment([5,6,2,1]))