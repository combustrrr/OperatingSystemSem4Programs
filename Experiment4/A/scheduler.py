import heapq
import time
from collections import deque

class PrintTask:
    def __init__(self, task_id, name, priority, execution_time):
        self.task_id = task_id
        self.name = name
        self.priority = priority  # Lower number means higher priority
        self.execution_time = execution_time  # Time required to complete the task
        self.remaining_time = execution_time  # Time left if preempted
    
    def __lt__(self, other):
        return self.priority < other.priority  # Ensures priority queue orders by priority

class PrintScheduler:
    def __init__(self):
        self.current_task = None
        self.task_queue = []  # Priority queue for new tasks
        self.waiting_queue = deque()  # Queue to resume preempted tasks
        self.time_elapsed = 0
    
    def add_task(self, task):
        heapq.heappush(self.task_queue, task)
        print(f"Task {task.task_id} ('{task.name}') added with priority {task.priority}.")
    
    def execute(self):
        while self.task_queue or self.waiting_queue or self.current_task:
            if self.task_queue and (not self.current_task or self.task_queue[0].priority < self.current_task.priority):
                if self.current_task:
                    print(f"Task {self.current_task.task_id} ('{self.current_task.name}') preempted.")
                    self.waiting_queue.append(self.current_task)
                
                self.current_task = heapq.heappop(self.task_queue)
                print(f"Executing task {self.current_task.task_id} ('{self.current_task.name}')...")
            
            if self.current_task:
                time_slice = min(5, self.current_task.remaining_time)  # Simulate time slice execution
                self.current_task.remaining_time -= time_slice
                self.time_elapsed += time_slice
                time.sleep(0.5)  # Simulating time delay
                print(f"Task {self.current_task.task_id} executed for {time_slice} minutes, remaining {self.current_task.remaining_time} minutes.")
                
                if self.current_task.remaining_time == 0:
                    print(f"Task {self.current_task.task_id} ('{self.current_task.name}') completed.")
                    self.current_task = None
            
            if not self.task_queue and self.waiting_queue and not self.current_task:
                self.current_task = self.waiting_queue.popleft()
                print(f"Resuming task {self.current_task.task_id} ('{self.current_task.name}').")

# User Input
if __name__ == "__main__":
    scheduler = PrintScheduler()
    
    while True:
        try:
            num_tasks = int(input("Enter the number of tasks: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the number of tasks.")
    for i in range(num_tasks):
        name = input(f"Enter name of task {i+1}: ")
        while True:
            try:
                priority = int(input(f"Enter priority (1-High, 2-Medium, 3-Low) for task {i+1}: "))
                if priority not in [1, 2, 3]:
                    print("Invalid input. Please enter a priority between 1 and 3.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter an integer for priority.")
        execution_time = int(input(f"Enter execution time (in minutes) for task {i+1}: "))
        scheduler.add_task(PrintTask(i+1, name, priority, execution_time))
    
    scheduler.execute()
