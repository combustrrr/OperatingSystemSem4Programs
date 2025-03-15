class Account:
    """Base account class without synchronization"""
    
    def __init__(self, account_id, initial_balance):
        self.account_id = account_id
        self.balance = initial_balance
        
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        current_balance = self.balance
        # Simulate some processing time that could cause race conditions
        import time
        time.sleep(0.1)
        
        self.balance = current_balance + amount
        return self.balance
        
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
            
        current_balance = self.balance
        # Simulate some processing time that could cause race conditions
        import time
        time.sleep(0.1)
        
        if current_balance < amount:
            raise ValueError("Insufficient funds")
            
        self.balance = current_balance - amount
        return self.balance
        
    def get_balance(self):
        return self.balance
