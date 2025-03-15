import threading
from semaphore_account import SemaphoreAccount

def atm_withdrawal(account, amount):
    """Simulate ATM withdrawal process"""
    account.withdraw(amount)
    print(f"ATM: Withdrew ${amount}")

def online_transfer(account, amount):
    """Simulate online banking transfer (withdrawal) process"""
    account.withdraw(amount)
    print(f"Online: Transferred ${amount}")

def branch_deposit(account, amount):
    """Simulate branch teller deposit process"""
    account.deposit(amount)
    print(f"Branch: Deposited ${amount}")

def main():
    try:
        initial_balance = float(input("Enter initial account balance: $"))
    except ValueError:
        print("Invalid input. Using default value.")
        initial_balance = 1000
    
    print(f"Initial Account Balance: ${initial_balance}")
    
    account = SemaphoreAccount("customer_account", initial_balance)
    
    try:
        atm_amount = float(input("Enter ATM withdrawal amount: $"))
    except ValueError:
        print("Invalid input. Using default value.")
        atm_amount = 500
        
    try:
        transfer_amount = float(input("Enter online transfer amount: $"))
    except ValueError:
        print("Invalid input. Using default value.")
        transfer_amount = 300
        
    try:
        deposit_amount = float(input("Enter branch deposit amount: $"))
    except ValueError:
        print("Invalid input. Using default value.")
        deposit_amount = 200
    
    # Create threads for the three processes
    atm_thread = threading.Thread(target=atm_withdrawal, args=(account, atm_amount))
    online_thread = threading.Thread(target=online_transfer, args=(account, transfer_amount))
    branch_thread = threading.Thread(target=branch_deposit, args=(account, deposit_amount))
    
    print("\nStarting concurrent transactions...")
    
    # Start all processes concurrently
    atm_thread.start()
    online_thread.start()
    branch_thread.start()
    
    # Wait for all processes to complete
    atm_thread.join()
    online_thread.join()
    branch_thread.join()
    
    final_balance = account.get_balance()
    print(f"Final Account Balance: ${final_balance}")

if __name__ == "__main__":
    main()
