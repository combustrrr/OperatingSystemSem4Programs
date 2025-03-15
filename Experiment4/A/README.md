# Print Shop Task Scheduler

This project implements a preemptive priority scheduler for a print shop that handles various printing tasks. The scheduler prioritizes tasks based on urgency and allows higher-priority tasks to preempt lower-priority ones.

## Features

- **Priority-Based Scheduling**:
  - High Priority: Walk-in customer jobs or urgent orders.
  - Medium Priority: Pre-scheduled corporate orders with deadlines.
  - Low Priority: Regular bulk printing jobs without strict deadlines.

- **Preemptive Scheduling**:
  - Higher-priority tasks can interrupt ongoing lower-priority tasks.
  - Preempted tasks resume once higher-priority tasks are completed.

- **Task Management**:
  - Tasks have varying execution times based on the type of printing.
  - Tasks of the same priority are executed in the order they arrive.
  - Idle time is minimized to maximize shop efficiency.
  - Input validation is implemented to ensure correct data types and priority values.

## Usage

1. Run the `scheduler.py` script.
2. Input task details when prompted. The script will handle invalid inputs and prompt you to enter them again:
   - Number of Tasks
   - Task Name
   - Priority (1: High, 2: Medium, 3: Low)
   - Execution time (in minutes)
3. The scheduler will execute tasks based on the defined rules.

## Example

```bash
python scheduler.py
