all_bank_accounts_info = []
    
# BankAccount class
class BankAccount:

    def __init__(self,interest_rate = 0.01,account_balance = 0): # Instance Constructor upon Instantiation
        self.interest_rate = interest_rate
        self.account_balance = account_balance
        all_bank_accounts_info.append(self)
        
    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self,amount):
        self.account_balance -= amount
        return self

    def display_account_info(self):
        print(f'Account Balance: {self.account_balance}')
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance = self.account_balance + (self.account_balance * self.interest_rate)
        return self

    @classmethod
    def print_all_bank_accounts_info(cls):
        for bank_account in all_bank_accounts_info:
            bank_account.display_account_info()
        return cls

# Create 2 accounts
account_gmj = BankAccount(0.05,50000)
account_aa = BankAccount(0.06,60000)

account_gmj.deposit(10000).deposit(5000).deposit(5000).withdraw(2500).yield_interest().display_account_info()

account_aa.deposit(10000).deposit(10000).withdraw(2500).withdraw(2500).withdraw(1250).withdraw(1250).yield_interest().display_account_info()

BankAccount.print_all_bank_accounts_info()