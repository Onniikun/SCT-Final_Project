__author__ = "Nathan Natoza"
__version__ = "1.1.2"
__credits__ = ""

import unittest 
from datetime import date
from bank_account.savings_account import SavingsAccount
# python -m unittest tests/test_savings_account.py

class TestSavingsAccount(unittest.TestCase):
    """
    Testing class for the Savings account file.
    """
    def setUp(self):
        self.savings = SavingsAccount(777, 320, 10000.00,
                                        date(2024, 12, 12), 100.00)
        
    def test_init_valid_argements_attributes_set(self):
        self.assertEqual(date(2024, 12, 12), 
                    self.savings._date_created)
        self.assertEqual(100.00, 
                    self.savings._SavingsAccount__minimum_balance)

    def test_init_invalid_minimum_balance_datatype(self):
        savings_account = SavingsAccount(777, 320, 10000.00,
                                        date(2024, 12, 12), "non")
        self.assertEqual(savings_account._SavingsAccount__minimum_balance, 50)

    def test_get_service_charge_balance_greater_minimum_balance_return(self):
        self.assertEqual(self.savings.get_service_charges(), 0.50)

    def test_get_service_charge_balance_equal_minimum_balance_return(self):
        savings_account = SavingsAccount(777, 320, 100.00,
                                        date(2024, 12, 12), 100.00)
        self.assertEqual(savings_account.get_service_charges(), 0.50)

    def test_get_service_charge_balance_less_than_minimum_balance_return(self):
        savings_account = SavingsAccount(777, 320, 10.00,
                                        date(2024, 12, 12), 100.00)
        self.assertEqual(savings_account.get_service_charges(), 1)

    def test_str_valid_inputs_formatted_string_return(self):
        expected = (f"Account Number: 777 Balance: $10,000.00\n" \
                    f"Minimum Balance: $100.00 " \
                    f"Account Type: Savings.")
        self.assertEqual(expected, str(self.savings)) 