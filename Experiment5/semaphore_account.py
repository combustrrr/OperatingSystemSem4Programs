from account import Account
import threading

class SemaphoreAccount(Account):
    """Account using binary semaphore for synchronization"""
    
    def __init__(self, account_id, initial_balance):
        super().__init__(account_id, initial_balance)
        self.semaphore = threading.Semaphore(1)  # Binary semaphore (mutex)
        
    def deposit(self, amount):
        self.semaphore.acquire()
        try:
            return super().deposit(amount)
        finally:
            self.semaphore.release()
    
    def withdraw(self, amount):
        self.semaphore.acquire()
        try:
            return super().withdraw(amount)
        finally:
            self.semaphore.release()
