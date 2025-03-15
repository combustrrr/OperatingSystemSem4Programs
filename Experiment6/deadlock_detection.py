import threading
import time

# Simplified resource and robot representation
class Resource:
    def __init__(self, name):
        self.name = name
        self.lock = threading.Lock()
        self.holder = None  # Robot holding the resource

class Robot:
    def __init__(self, name):
        self.name = name
        self.holding = None  # Resource being held by the robot
        self.waiting_for = None # Resource the robot is waiting for

# Initialize resources and robots
welding_station = Resource("Welding Station")
painting_unit = Resource("Painting Unit")
conveyor = Resource("Conveyor")

R1 = Robot("R1")
R2 = Robot("R2")
R3 = Robot("R3")

resources = {welding_station.name: welding_station, painting_unit.name: painting_unit, conveyor.name: conveyor}
robots = {R1.name: R1, R2.name: R2, R3.name: R3}

# Function to detect deadlocks
def detect_deadlock():
    """Detect deadlocks by checking for circular waits in the resource allocation graph."""
    for robot in robots.values():
        if robot.holding is None and robot.waiting_for is not None:
            # Check if the robot is waiting for a resource held by another robot
            holder = robot.waiting_for.holder
            if holder is not None and holder.waiting_for == robot.holding:
                print("Deadlock detected!")
                print(f"{robot.name} is waiting for {robot.waiting_for.name} held by {holder.name}")
                print(f"{holder.name} is waiting for {holder.waiting_for.name} held by {robot.name}")
                return True
    return False

# Simulate resource acquisition
def acquire_resource(robot, resource):
    print(f"{robot.name}: Attempting to acquire {resource.name}")
    with resource.lock:
        resource.holder = robot
        robot.holding = resource
        print(f"{robot.name}: Acquired {resource.name}")
        time.sleep(1)  # Simulate work

def release_resource(robot, resource):
    resource.holder = None
    robot.holding = None
    print(f"{robot.name}: Released {resource.name}")

# Simulate robot tasks with potential deadlock
def robot_task(robot, resource1_name, resource2_name):
    resource1 = resources[resource1_name]
    resource2 = resources[resource2_name]

    # First resource
    acquire_resource(robot, resource1)
    robot.waiting_for = resource2 # Indicate what robot is waiting for
    time.sleep(0.5)

    # Second resource - potential deadlock
    print(f"{robot.name}: Waiting for {resource2.name}")
    with resource2.lock: # Attempt to acquire the lock
        if resource2.holder is not None:
            print(f"{robot.name} waiting for {resource2.name} held by {resource2.holder.name}")
            if detect_deadlock():
                print("Deadlock detected, attempting to resolve...")
                # In a real system, you might implement a deadlock resolution strategy here
                # For example, release one of the resources
        acquire_resource(robot, resource2)

    release_resource(robot, resource1)
    release_resource(robot, resource2)
    print(f"{robot.name}: Task completed")

# Create threads
t1 = threading.Thread(target=robot_task, args=(R1, welding_station.name, painting_unit.name))
t2 = threading.Thread(target=robot_task, args=(R2, painting_unit.name, conveyor.name))
t3 = threading.Thread(target=robot_task, args=(R3, conveyor.name, welding_station.name))

# Start threads
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All tasks completed")
