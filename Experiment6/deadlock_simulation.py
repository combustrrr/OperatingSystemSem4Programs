import threading
import time
import random

# Define the resources
resources = {
    'Welding Station': threading.Lock(),
    'Painting Unit': threading.Lock(),
    'Conveyor': threading.Lock()
}

# Define the robots
robots = ['R1', 'R2', 'R3']

def task(robot_name, resource_need1, resource_need2):
    while True:
        print(f"{robot_name}: Trying to acquire {resource_need1}")
        with resources[resource_need1]:
            print(f"{robot_name}: Acquired {resource_need1}")
            time.sleep(random.randint(1, 3))  # Simulate some work

            print(f"{robot_name}: Trying to acquire {resource_need2}")
            resource2_acquired = resources[resource_need2].acquire(timeout=2)  # Try to acquire with timeout
            if resource2_acquired:
                try:
                    print(f"{robot_name}: Acquired {resource_need2}")
                    time.sleep(random.randint(1, 3))  # Simulate some work
                finally:
                    resources[resource_need2].release()
                    print(f"{robot_name}: Releasing {resource_need2}")
                print(f"{robot_name}: Releasing {resource_need1}")
                print(f"{robot_name}: Task completed")
                return  # Task completed successfully
            else:
                print(f"{robot_name}: Failed to acquire {resource_need2}, retrying")
                time.sleep(1)  # Wait before retrying

# Create threads for each robot
threads = []
threads.append(threading.Thread(target=task, args=('R1', 'Welding Station', 'Painting Unit')))
threads.append(threading.Thread(target=task, args=('R2', 'Painting Unit', 'Conveyor')))
threads.append(threading.Thread(target=task, args=('R3', 'Conveyor', 'Welding Station')))

# Start the threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All tasks completed.")
