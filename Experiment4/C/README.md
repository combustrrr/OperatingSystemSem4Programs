# Game Server with Round Robin Scheduling

This Python script simulates a game server that handles game sessions for multiple players simultaneously. Each player's actions generate tasks that must be processed by the server. To ensure fairness and a smooth gaming experience, the server allocates CPU time to player tasks using the Round Robin scheduling algorithm.

## Features

- Each player generates tasks that require CPU time to process game actions.
- Tasks vary in complexity and execution time depending on the player's actions (e.g., simple movement vs. complex combat calculations).
- The server uses a fixed time slice (e.g., 50 ms per player) to process tasks.
- If a task is not completed within the allocated time slice, it is paused and placed back in the queue.
- Tasks are processed in the order they are queued.
- The server ensures fairness and avoids favoring any single player.

## Usage

1. Run the script:
    ```sh
    python game_server.py
    ```

2. Enter the number of player tasks when prompted.

3. For each task, enter the Player ID and the execution time (in milliseconds).

4. The server will process the tasks using the Round Robin scheduling algorithm and display the execution details.

## Example

```
Enter the number of player tasks: 3
Enter Player ID for task 1: Player1
Enter execution time (in ms) for task 1: 100
Enter Player ID for task 2: Player2
Enter execution time (in ms) for task 2: 150
Enter Player ID for task 3: Player3
Enter execution time (in ms) for task 3: 200

Task 1 from Player Player1 added with execution time 100 ms.
Task 2 from Player Player2 added with execution time 150 ms.
Task 3 from Player Player3 added with execution time 200 ms.
Executed Task 1 from Player Player1 for 50 ms, remaining 50 ms.
Executed Task 2 from Player Player2 for 50 ms, remaining 100 ms.
Executed Task 3 from Player Player3 for 50 ms, remaining 150 ms.
Executed Task 1 from Player Player1 for 50 ms, remaining 0 ms.
Task 1 from Player Player1 completed.
Executed Task 2 from Player Player2 for 50 ms, remaining 50 ms.
Executed Task 3 from Player Player3 for 50 ms, remaining 100 ms.
Executed Task 2 from Player Player2 for 50 ms, remaining 0 ms.
Task 2 from Player Player2 completed.
Executed Task 3 from Player Player3 for 50 ms, remaining 50 ms.
Executed Task 3 from Player Player3 for 50 ms, remaining 0 ms.
Task 3 from Player Player3 completed.
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License.