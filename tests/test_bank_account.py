"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
__author__ = "ACE Faculty"
__version__ = "1.4.0"
__credits__ = "Nathan Natoza"

import unittest
from bank_account.bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    """
    Testing class for the Bank Account file.
    """
    def setUp(self):
        self.bank = BankAccount(777, 320, 10000.00)

    def test_init_valid_arguments_attributes_set(self):
        bankaccount = BankAccount(777, 320, 10000.00)
        
        self.assertEqual(777, bankaccount._BankAccount__account_number)
        self.assertEqual(320, bankaccount._BankAccount__client_number)
        self.assertEqual(10000.00, bankaccount._BankAccount__balance)
    
    def test_init_account_number_raises_valueerror(self):
        with self.assertRaises(ValueError):
            bankaccount = BankAccount("non", 320, 10000.00)

    def test_init_client_number_raises_valueerror(self):
        with self.assertRaises(ValueError):
            bankaccount = BankAccount(777, "non", 10000.00)
            
    def test_init_balance_attibutes_set_to_non_numeric_return_zero(self):
        bankaccount = BankAccount(777, 320, "non")
        self.assertEqual(bankaccount._BankAccount__balance, 0)


#--PEP8-Standards-Line--------------------------------------------------------

    def test_account_number_accessor_valid_return(self):
        self.assertEqual(777, self.bank.account_number)

    def test_client_number_accessor_valid_return(self):
        self.assertEqual(320, self.bank.client_number)
    
    def test_balance_accessor_valid_return(self):
        self.assertEqual(10000.00, self.bank.balance)

    def test_update_balance_added_amount_value_return(self):
        amount = self.bank
        updated_balance = amount.update_balance(100)
        self.assertEqual(updated_balance, 10100.00)

    def test_update_balance_negative_amount_value_return(self):
        amount = self.bank
        updated_balance = amount.update_balance(-100)
        self.assertEqual(updated_balance, 9900.00)

    def test_update_balance_non_numeric_amount_value_return(self):
        amount = self.bank
        updated_balance = amount.update_balance("")
        self.assertEqual(updated_balance, 10000.00)   

    def test_deposit_positive_balance_value_added_return(self):
        amount = self.bank
        amount.deposit(100)
        self.assertEqual(amount.balance, 10100.00)

    def test_deposit_negative_balance_value_added_return(self):
        amount = self.bank
        with self.assertRaises(ValueError) as context:
            amount.deposit(-100)
        text = "Deposit amount: $-100.00 must be positive"
        self.assertEqual(str(context.exception), text)
    
    def test_withdraw_positive_balance_value_added_return(self):
        amount = self.bank
        amount.withdraw(100)
        self.assertEqual(amount.balance, 9900.00)
    
    def test_withdraw_negative_balance_value_added_return(self):
        amount = self.bank
        with self.assertRaises(ValueError) as context:
            amount.withdraw(-100)
        text = "Withdrawal amount: $-100.00 must be positive."
        self.assertEqual(str(context.exception), text)

    def test_withdraw_amount_exceed_balance_value_withdrawl_return(self):
        amount = self.bank
        with self.assertRaises(ValueError) as context:
            amount.withdraw(100000)
        text = "Withdrawal amount: $100,000.00 must " \
        "not exceed the account balance: $10,000.00"
        self.assertEqual(str(context.exception), text)

    def test_str_valid_inputs_formatted_string_return(self):
        expected = ("Account Number: 777 Balance: $10,000.00")
        self.assertEqual(expected, str(self.bank))         

