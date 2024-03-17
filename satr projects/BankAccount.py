'''
import datetime
class BankAccount :
    def __init__ (self):
        self.balance=0
    
    def deposit(self, amount):
        self.balance +=amount
        self.print_transaction('Deposit ', amount)


    def withdrow(self, amount):
       if(self.balance <=0):
        print ('sorry, there is no money in the account ')
       else :
            if (self.balance-amount) >=0:
                 self.balance-=amount
                 self.print_transaction('Withdrawal', amount)

            else:
                print('sorry, the amnout of balance is not enough ')
    
    
    def check_balance(self):
        print("current balance : " , self.balance )    

    def print_transaction(self, funcion_type,amount):
        timestamp= datetime.datetime.now().strftime("%Y-%M-%D %H:%M:%S")
        print(f"{funcion_type} of {amount} occurred at {timestamp}")

user_account = BankAccount()

user_account.check_balance()

user_account.deposit(100)
user_account.deposit(100)
user_account.check_balance()






import datetime

class BankAccount:
    
   # def __init__(self):
    #    global balance = 0
        
     
    def deposit(self, amount):
        global balance 
        balance += amount
        self.print_transaction('Deposit', amount)

    def withdraw(self, amount):
        global balance 
        if balance <= 0:
            print('Sorry, there is no money in the account')
        else:
            if balance - amount >= 0:
                balance -= amount
                self.print_transaction('Withdrawal', amount)
            else:
                print('Sorry, the amount of balance is not enough')
    
    def check_balance(self):
        global balance 
        print("Current balance:", balance)

    def print_transaction(self, function_type, amount):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{function_type} of {amount} occurred at {timestamp}")

balance = 0
user_account = BankAccount()

user_account.deposit(100)
#user_account.withdraw(500)
user_account.check_balance()

import datetime

class BankAccount:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        self.print_transaction('Deposit', amount)

    def withdraw(self, amount):
        if self.balance <= 0:
            print('Sorry, there is no money in the account')
        else:
            if self.balance - amount >= 0:
                self.balance -= amount
                self.print_transaction('Withdrawal', amount)
            else:
                print('Sorry, the amount of balance is not enough')
    
    def check_balance(self):
        print("Current balance:", self.balance)

    def print_transaction(self, function_type, amount):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{function_type} of {amount} occurred at {timestamp}")


user_account = BankAccount()

user_account.deposit(400)
user_account.deposit(100)
user_account.check_balance()


'''


import datetime

class BankAccount:
    def __init__(self):
        self.balance = self.load_balance()
    
    def deposit(self, amount):
        self.balance += amount
        self.save_balance()
        self.print_transaction('Deposit', amount)

    def withdraw(self, amount):
        if self.balance <= 0:
            print('Sorry, there is no money in the account')
        else:
            if self.balance - amount >= 0:
                self.balance -= amount
                self.save_balance()
                self.print_transaction('Withdrawal', amount)
            else:
                print('Sorry, the amount of balance is not enough')
    
    def check_balance(self):
        print("Current balance:", self.balance)

    def print_transaction(self, function_type, amount):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{function_type} of {amount} occurred at {timestamp}")

    def save_balance(self):
        with open('balance.txt', 'w') as file:
            file.write(str(self.balance))

    def load_balance(self):
        try:
            with open('balance.txt', 'r') as file:
                return int(file.read())
        except FileNotFoundError:
            return 0


user_account = BankAccount()

user_account.deposit(400)
user_account.deposit(100)
user_account.check_balance()