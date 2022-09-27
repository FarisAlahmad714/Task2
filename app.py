class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate =0.01 , balance = 0 ): 
        self.int_rate = int_rate
        self.balance = balance
        self.yield_interest()
        
#increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount
        return self
#decreases the account balance by the given amount if there are 
# sufficient funds; if there is not enough money, print
# a message "Insufficient funds: Charging a $5 fee" and deduct $5

    def withdraw(self, amount):
        if self.balance <= amount:
            self.balance -=5
            print(f'{self.balance}' + " insuffecient")
        else:
            self.balance = amount 
            print('You have withdrawed')
            
#print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print('Balance:' , self.balance)
        return self

#increases the account balance by the current balance * 
# the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1+self.int_rate)
            
        return self

user1=BankAccount(.05)
print(user1.int_rate)
user1.display_account_info().deposit(70).withdraw(50)