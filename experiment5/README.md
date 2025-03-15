# Banking System - Critical Section Problem Solution

This project demonstrates how to solve the critical section problem in a banking system using semaphores.

## The Problem

In a banking system, multiple processes (ATM withdrawals, online transfers, and in-branch deposits) can access and modify account balances concurrently. Without proper synchronization, this creates a critical section problem that can lead to race conditions and inconsistent account balances.

### Example Scenario

Consider an account with an initial balance of $1000 and three concurrent transactions:
1. ATM Process: Withdraw $500
2. Online Banking Process: Transfer (withdraw) $300
3. Branch Teller Process: Deposit $200

Without synchronization, all processes might read the initial balance of $1000 simultaneously:
- The ATM would set the balance to $500 ($1000 - $500)
- The online transfer would set the balance to $700 ($1000 - $300)
- The branch deposit would set the balance to $1200 ($1000 + $200)

Depending on which process finishes last, the final balance would be incorrect ($500, $700, or $1200) instead of the correct balance of $400 ($1000 - $500 - $300 + $200).

## The Solution: Semaphores

Our implementation uses binary semaphores to ensure mutual exclusion when accessing the shared account balance. This guarantees that only one process can be in the critical section at any time.

### How Semaphores Work in Detail

1. **Binary Semaphore Implementation**:
   - A semaphore is initialized with a value of 1 (indicating one resource available)
   - The `acquire()` method decrements the counter and blocks if it's already 0
   - The `release()` method increments the counter, potentially unblocking waiting processes

2. **Protection Mechanism**:
   - Before any thread accesses the account balance, it must call `semaphore.acquire()`
   - If another thread already holds the semaphore, the new thread will wait (block)
   - After completing its operation, the thread calls `semaphore.release()` to allow others to proceed

3. **Transaction Flow with Semaphores**:
   ```
   Thread 1 (ATM):                Thread 2 (Online):             Thread 3 (Branch):
   acquire semaphore              (waiting for semaphore)        (waiting for semaphore)
   read balance ($1000)
   calculate ($1000-$500)
   update balance ($500)
   release semaphore
                                  acquire semaphore              (waiting for semaphore)
                                  read balance ($500)
                                  calculate ($500-$300)
                                  update balance ($200)
                                  release semaphore
                                                                acquire semaphore
                                                                read balance ($200)
                                                                calculate ($200+$200)
                                                                update balance ($400)
                                                                release semaphore
   ```

4. **Final Balance Calculation**:
   - Because of the semaphore, each transaction sees the current balance after previous transactions
   - The transactions execute in sequence (even though they're launched concurrently)
   - The final balance correctly reflects all operations: $1000 - $500 - $300 + $200 = $400

### Code Implementation

The critical section protection is implemented in the `SemaphoreAccount` class:

```python
def deposit(self, amount):
    self.semaphore.acquire()  # Lock the critical section
    try:
        # Only one thread can execute this code at a time
        current_balance = self.balance
        # Simulate processing time
        time.sleep(0.1)
        self.balance = current_balance + amount
        return self.balance
    finally:
        self.semaphore.release()  # Unlock the critical section
```

This pattern ensures that:
1. The entire operation (reading balance, calculating new amount, updating) is atomic
2. No other thread can interleave its operations between our read and write
3. Each transaction sees a consistent view of the account data

## Sample Output

Below is a screenshot showing the execution of the program with the semaphore solution:

![Program Output](/workspaces/TestRun/experiment5/Screenshot%202025-03-15%20201916.png)

The screenshot demonstrates how the program:
1. Accepts user input for initial balance and transaction amounts
2. Executes the transactions concurrently but with semaphore protection
3. Shows the correct final balance that reflects all transactions

## How to Verify the Solution Works

When you run the simulation:
1. All three transaction processes attempt to run concurrently
2. The semaphore forces them to execute their critical sections one at a time
3. The final balance will always be $400 (for the default example values)
4. Without the semaphore, the final balance would be unpredictable and often incorrect

## Files in this Project

- `account.py`: Base account class without synchronization
- `semaphore_account.py`: Account implementation using semaphores for synchronization
- `simulation.py`: Script that simulates concurrent account transactions

## How to Run

```bash
python simulation.py
```

The program will prompt you for:
1. Initial account balance
2. ATM withdrawal amount
3. Online transfer amount
4. Branch deposit amount

It will then execute these transactions concurrently with semaphore protection.
