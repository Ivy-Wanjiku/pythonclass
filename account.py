class Account:
    def __init__(self,number,pin,owner=None):
        self.number=number
        self.__pin=pin
        self.__balance=0
        self.owner = owner
        self.overdraft_limit = None
        self.minimum_balance = None
        self.is_frozen = False
        self.transactions = []
    def show_balance(self,pin):
        if pin==self.__pin:
            return self.__balance
        else:
            return "Wrong pin"
    def deposit(self,amount,pin):
        if pin==self.__pin:
            self.__balance+=amount
            self.transactions.append(f"Deposit: {amount}")
            return f"ksh {amount} was deposited successfully.Current balance is ksh {self.__balance}"
        else:
            return f"Please enter the correct pin"
    def withdraw(self,amount,pin):
        if pin==self.__pin:
            if self.__balance <=600:
                return f"The balance  is so small to be withdrawn.The limit is 600"
            else:
                self.__balance-=amount 
                self.transactions.append(f"Withdrawal: {amount}")
                return f"You have succefully withdrawn {amount} new balance is {self.__balance}"
        else:
            return f"Input the correct pin"
    def view_details(self, pin):
        if pin!= self.__pin:
            return "Incorrect Pin"
        else:
            return {
                "Owner":self.owner,
                "balance":self.__balance,
                "over_draft":self.overdraft_limit,
                "minimum_balance":self.is_frozen,
                "transactions":self.transactions
        }
    def change_owner(self, new_owner, pin):
        if pin!= self.__pin:
            return "Incorrect Pin"
        self.owner = new_owner
        return f"Account owner changed to {new_owner}"
    def account_statement(self, pin):
        if pin!= self.__pin:
            return "Incorrect Pin"
        return "\n".join(self.transactions)
    def set_overdraft_limit(self, limit, pin):
        if pin!= self.__pin:
            return "Incorrect Pin"
        self.overdraft_limit = limit
        return f"Overdraft limit set to {limit}"
    def interest_calculation(self, rate, pin):
        if pin!= self.__pin:
            return "Incorrect Pin"
        interest = self.__balance * rate / 100
        self.__balance += interest
        self.transactions.append(f"Interest added: {interest}")
        return f"Interest calculated and applied. New balance: {self.__balance}"
    def freeze_acc(self, pin):
        if pin!= self.__pin:
            return "Incorect Pin"
        self.is_frozen = True
        return "Account frozen"
    def unfreeze_acc(self, pin):
        if pin!= self.__pin:
            return "Incorrect Pin"
        self.is_frozen = False
        return "Account unfrozen"
    def transaction_history(self, pin):
        if pin!= self.__pin:
            return "Incorrect Pin"
        return self.transactions
    def set_minimum_bal(self, min_balance, pin):
        if pin!= self.__pin:
            return "Incorrect Pin"
        self.minimum_balance = min_balance
        return f"Minimum balance set to {min_balance}"
    def transfer_funds(self, recipient_number, amount, pin):
        if pin!= self.__pin: 
            return "Incorrect Pin"
        if self.is_frozen:
            return "Account is frozen"
        if amount > self.__balance + (self.overdraft_limit if self.overdraft_limit else 0):
            return "Insufficient funds"
       
        return f"Funds transferred successfully. New balance: {self.__balance - amount}"
    def close_acc(self, pin):
        if pin!= self.__pin:
            return "Incorrect Pin"

        return "Account closed"
    
            




