class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.account_number}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def check_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")

# Example usage:
if __name__ == "__main__":
    account1 = BankAccount("123456", 1000)
    account2 = BankAccount("789012")

    account1.deposit(500)
    account1.check_balance()

    account1.withdraw(200)
    account1.check_balance()

    account2.deposit(1000)
    account2.check_balance()

    account2.withdraw(500)
    account2.check_balance()
3/;