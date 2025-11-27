"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.1.0"
__credits__ = "Nathan Natoza"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client

from bank_account import *
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from client.client import *
from datetime import date, timedelta


# 2. Create a Client object with data of your choice.
try: 
    client = Client(404, "Nathan", "Natoza", "NatNat@email.ca")
except ValueError as e:
        print(e)

# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
try:
    chequing_account = ChequingAccount(7301, client.client_number, 120.00,
                                date(2004, 12, 12), 100.00, 0.05)
except ValueError as e:
        print(e)
try:
    saving_account = SavingsAccount(7302, client.client_number, 140.00,
                                date(2012, 5, 16), 10.00)
except ValueError as e:
        print(e)
# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).

chequing_account.attach(client)
saving_account.attach(client)


# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.

try:
    client_2 = Client(123, "Dominick", "Monserrate", "DomMon@email.ca")
except ValueError as e:
        print(e)

try:
    saving_account_2 = SavingsAccount(7303, client_2.client_number, 112.00,
                                date(2017, 1, 6), 10.00)
except ValueError as e:
        print(e)

saving_account_2.attach(client_2)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.
try:
    chequing_account.deposit(12000)
except ValueError as e:
        print(e)

try:
    chequing_account.withdraw(10005)
except ValueError as e:
        print(e)


try:
    saving_account.withdraw(100)
except ValueError as e:
        print(e)

try:
    saving_account_2.deposit(10000)
except ValueError as e:
        print(e)

try:
    chequing_account.deposit(32)
except ValueError as e:
        print(e)
      