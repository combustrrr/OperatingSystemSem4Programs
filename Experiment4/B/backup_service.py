import heapq
import time

class BackupJob:
    def __init__(self, job_id, arrival_time, transfer_time):
        self.job_id = job_id
        self.arrival_time = arrival_time
        self.transfer_time = transfer_time
        self.remaining_time = transfer_time  # Time left if preempted
    
    def __lt__(self, other):
        return self.remaining_time < other.remaining_time  # Shortest job first (SJF)

class BackupScheduler:
    def __init__(self):
        self.current_job = None
        self.job_queue = []  # Min-heap for backup jobs
        self.time_elapsed = 0
    
    def add_job(self, job):
        heapq.heappush(self.job_queue, job)
        print(f"Job {job.job_id} added with transfer time {job.transfer_time} minutes.")
    
    def execute(self):
        while self.job_queue or self.current_job:
            if self.job_queue and (not self.current_job or self.job_queue[0].remaining_time < self.current_job.remaining_time):
                if self.current_job:
                    print(f"Job {self.current_job.job_id} preempted.")
                    heapq.heappush(self.job_queue, self.current_job)
                
                self.current_job = heapq.heappop(self.job_queue)
                print(f"Executing job {self.current_job.job_id}...")
            
            if self.current_job:
                time_slice = min(5, self.current_job.remaining_time)  # Simulate execution
                self.current_job.remaining_time -= time_slice
                self.time_elapsed += time_slice
                time.sleep(0.5)  # Simulating time delay
                print(f"Job {self.current_job.job_id} executed for {time_slice} minutes, remaining {self.current_job.remaining_time} minutes.")
                
                if self.current_job.remaining_time == 0:
                    print(f"Job {self.current_job.job_id} completed.")
                    self.current_job = None

# User Input
if __name__ == "__main__":
    scheduler = BackupScheduler()
    
    num_jobs = int(input("Enter the number of backup jobs: "))
    for i in range(num_jobs):
        arrival_time = int(input(f"Enter arrival time for job {i+1}: "))
        transfer_time = int(input(f"Enter estimated transfer time (in minutes) for job {i+1}: "))
        scheduler.add_job(BackupJob(i+1, arrival_time, transfer_time))
    
    scheduler.execute()