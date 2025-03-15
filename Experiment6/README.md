## Experiment 6: Deadlock Simulation and Detection in a Robotic Assembly Line

### Overview

This experiment simulates a robotic assembly line where multiple robots work together to assemble products. Each robot requires access to multiple resources (e.g., tools, parts) to complete its tasks. A deadlock situation can occur if robots hold onto resources while waiting for other resources held by other robots. The goal is to simulate this scenario and implement a deadlock detection mechanism to identify and resolve deadlocks.

### Files

-   `deadlock_simulation.py`: Contains the code to simulate the robotic assembly line and the potential for deadlocks.
-   `deadlock_detection.py`: Contains the code to detect deadlocks by checking for circular waits in the resource allocation graph.

### How to Run

1.  Ensure you have Python installed.
2.  Navigate to the `Experiment6` directory.
3.  Run the simulation: `python deadlock_simulation.py`
4.  Run the deadlock detection: `python deadlock_detection.py`

### Implementation Details

The `deadlock_simulation.py` script uses threads to simulate robots and locks to represent resources. Robots attempt to acquire resources in a specific order, which can lead to deadlocks. A timeout mechanism is implemented to prevent the simulation from hanging indefinitely.

The `deadlock_detection.py` script implements a resource allocation graph and detects circular waits to identify deadlocks. When a deadlock is detected, a message is printed to the console.

### Output

The scripts will print messages to the console indicating when robots acquire and release resources, and when deadlocks are detected.
