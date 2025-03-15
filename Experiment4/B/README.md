# Backup Service

This project implements a backup service that schedules and executes backup jobs using a preemptive shortest job first (SJF) scheduling algorithm.

## Files

- `backup_service.py`: Contains the implementation of the backup job and scheduler.

## Classes

### BackupJob

Represents a backup job with the following attributes:
- `job_id`: Unique identifier for the job.
- `arrival_time`: The time at which the job arrives.
- `transfer_time`: The estimated time required to complete the job.
- `remaining_time`: The remaining time to complete the job (used for preemption).

### BackupScheduler

Manages the scheduling and execution of backup jobs. It uses a min-heap to prioritize jobs with the shortest remaining time.

#### Methods

- `add_job(job)`: Adds a new job to the scheduler.
- `execute()`: Executes the jobs based on the SJF scheduling algorithm.

## Usage

1. Run the `backup_service.py` script.
2. Enter the number of backup jobs.
3. For each job, enter the arrival time and the estimated transfer time.
4. The scheduler will execute the jobs and print the status of each job.

## Example

```sh
$ python backup_service.py
Enter the number of backup jobs: 2
Enter arrival time for job 1: 0
Enter estimated transfer time (in minutes) for job 1: 10
Job 1 added with transfer time 10 minutes.
Enter arrival time for job 2: 1
Enter estimated transfer time (in minutes) for job 2: 5
Job 2 added with transfer time 5 minutes.
Executing job 2...
Job 2 executed for 5 minutes, remaining 0 minutes.
Job 2 completed.
Executing job 1...
Job 1 executed for 5 minutes, remaining 5 minutes.
Job 1 executed for 5 minutes, remaining 0 minutes.
Job 1 completed.
```

## Notes

- The scheduler uses a time slice of 5 minutes for job execution.
- The script simulates time delay using `time.sleep(0.5)` to represent the passage of time.