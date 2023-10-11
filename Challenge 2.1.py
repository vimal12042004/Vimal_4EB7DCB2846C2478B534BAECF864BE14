class BankAccount:
  def __init_(self, account_number, account_holder_name, initial_balance=0.0):
self._account_number= account number
self._account_holder_name = account_holder_name
self._account_balance initial_balance
def deposit(self, amount):
  if amount>0:
    self._account balance+=amount
    print("Deposited {). New balance: {}".format(amount,self._account_balance))
  else:
    print("Invalid deposit amount. Please deposit a positive amount")
      def withdraw(self, amount):
        if amount >0 and amount <=
        self.___account_balance:
          self._account balance -= amount
          print("withdraw (). New balance: (}".format(amount,self._account_balance))
        else:
          print("Invalid withdrawl amount or insufficient balance.")
def display balance(self):
print("Account balance for () (Account #)): (}".format(self._account_holder_name,number, self._account_balance))
self._account_nu

account = BankAccount(account_number="12345678",account_holder_name="Vishnu",initial_balance=1000.0

account.display_balance()

account.deposit(500.0) 
account withdraw(200.0)
account.display_balance().Not
