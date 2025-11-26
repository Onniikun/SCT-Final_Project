"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.1.1"
__credits__ = "Nathan Natoza"

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from datetime import date
from bank_account.bank_account import BankAccount
from bank_account.chequing_account import ChequingAccount
from bank_account.investment_account import InvestmentAccount
from bank_account.savings_account import SavingsAccount


# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
try:
    chequing_account = ChequingAccount(7301, 5149, 99.00,
                                date(2017, 4, 12), 100.00, 0.05)
except ValueError as e:
    print(e)

# 3. Print the ChequingAccount created in step 2.
print(chequing_account)

# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
calculated_service_charge = chequing_account.get_service_charges()
print(f"Service Charge: ${calculated_service_charge:.2f}")

# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
chequing_account.deposit(1001.00)

# 4b. Print the ChequingAccount
print(chequing_account)

# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
calculated_service_charge = chequing_account.get_service_charges()
print(f"Service Charge: ${calculated_service_charge:.2f}")

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
try:
    saving_account = SavingsAccount(7302, 5150, 99.00,
                                date(2017, 4, 12), 10.00)
except ValueError as e:
    print(e)

# 6. Print the SavingsAccount created in step 5.
print(saving_account)

# # 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
calculated_service_charge = saving_account.get_service_charges()
print(f"Service Charge: ${calculated_service_charge:.2f}")


# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
saving_account.withdraw(90.00)

# 7b. Print the SavingsAccount.
print(saving_account)

# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
calculated_service_charge = saving_account.get_service_charges()
print(f"Service Charge: ${calculated_service_charge:.2f}")


print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
try:
    investment_account = InvestmentAccount(7303, 5151, 2000.00,
                                date(2017, 4, 12), 2.00)
except ValueError as e:
    print(e)

# 9a. Print the InvestmentAccount created in step 8.
print(investment_account)

# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
calculated_service_charge = investment_account.get_service_charges()
print(f"Service Charge: ${calculated_service_charge:.2f}")

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
try:
    investment_account_2 = InvestmentAccount(7304, 5151, 2000.00,
                                date(2002, 4, 12), 10.00)
except ValueError as e:
    print(e)

# 11a. Print the InvestmentAccount created in step 10.
print(investment_account_2)

# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
calculated_service_charge = investment_account_2.get_service_charges()
print(f"Service Charge: ${calculated_service_charge:.2f}")

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
try:
    chequing_account.withdraw(chequing_account.get_service_charges())
    saving_account.withdraw(saving_account.get_service_charges())
    investment_account.withdraw(investment_account.get_service_charges())
    investment_account.withdraw(investment_account_2.get_service_charges())
except ValueError as e:
    print(e)


# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print(chequing_account)
print(saving_account)
print(investment_account)
print(investment_account_2)
