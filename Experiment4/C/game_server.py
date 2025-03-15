import time
from collections import deque

class GameTask:
    def __init__(self, player_id, task_id, execution_time):
        self.player_id = player_id
        self.task_id = task_id
        self.execution_time = execution_time
        self.remaining_time = execution_time  # Time left if preempted
    
class RoundRobinScheduler:
    def __init__(self, time_slice=50):
        self.task_queue = deque()
        self.time_slice = time_slice  # Time slice in milliseconds
    
    def add_task(self, task):
        self.task_queue.append(task)
        print(f"Task {task.task_id} from Player {task.player_id} added with execution time {task.execution_time} ms.")
    
    def execute(self):
        while self.task_queue:
            current_task = self.task_queue.popleft()
            execution_time = min(self.time_slice, current_task.remaining_time)
            current_task.remaining_time -= execution_time
            time.sleep(execution_time / 1000)  # Simulating time delay in seconds
            print(f"Executed Task {current_task.task_id} from Player {current_task.player_id} for {execution_time} ms, remaining {current_task.remaining_time} ms.")
            
            if current_task.remaining_time > 0:
                self.task_queue.append(current_task)  # Re-add the task if not completed
            else:
                print(f"Task {current_task.task_id} from Player {current_task.player_id} completed.")

# User Input
if __name__ == "__main__":
    scheduler = RoundRobinScheduler()
    
    num_tasks = int(input("Enter the number of player tasks: "))
    for i in range(num_tasks):
        player_id = input(f"Enter Player ID for task {i+1}: ")
        execution_time = int(input(f"Enter execution time (in ms) for task {i+1}: "))
        scheduler.add_task(GameTask(player_id, i+1, execution_time))
    
    scheduler.execute()
